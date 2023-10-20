#
# Direct test mode for nRF5340 with nRF21540 (BL5340PA)
#
# SPDX-License-Identifier: LicenseRef-LairdConnectivity-Clause
#
import ctypes
from enum import Enum
import logging
from power_table import POWER_TABLE
import math
import serial
import time

logger = logging.getLogger(__name__)

uint16_t = ctypes.c_uint16


BAUD_RATE = 19200
SERIAL_TIMEOUT_SECONDS = 1
RESPONSE_SIZE = 2
CHANNEL_MIN = 0
CHANNEL_MAX = 39
FREQ_MIN = 2402
FREQ_MAX = 2480
COMMAND_FREQ_OR_LEN_MAX = 63
PACKET_LENGTH_LOWER_MAX = COMMAND_FREQ_OR_LEN_MAX
PACKET_LENGTH_UPPER_MAX = 3
PACKET_LENGTH_MAX = 255

NRF5340_SOC_PWR_TABLE = [0, -1, -2, -3, -4, -5, -6, -7, -8, -12, -16, -20, -40]
"""Power levels supported by nRF5340 System on a Chip (SoC)"""


class CommandType(Enum):
    """
    The four command types described by the Bluetooth®
    Core Specification: Version 5.2, Vol. 6, Part F.
    """

    TEST_SETUP = 0  # formerly named reset
    """Configure the device under test"""
    RX = 1
    """Start Receive test"""
    TX = 2
    """Start a transmit test"""
    END = 3
    """End Rx/Tx Test"""


class TestSetup(Enum):
    """
    Subcommands of the Test Setup command.
    """

    RESET = 0
    SET_UPPER = 1
    SET_PHY = 2
    SELECT_MODULATION = 3
    READ_SUPPORTED = 4
    READ_MAX = (5,)
    CONSTANT_TONE_EXTENSION = 6
    CONSTANT_TONE_EXTENSION_SLOT = 7
    ANTENNA_ARRAY = 8
    TRANSMIT_POWER = 9


# This was simplified from the specification because
# for the Nordic nRF5340, min/max are the same.
class Phy(Enum):
    PHY_1M = 7
    PHY_2M = 11
    CODED_PHY_S8 = 15
    CODED_PHY_S2 = 19


class Antenna(Enum):
    INTERNAL = (0,)
    EXTERNAL = 1


class Region(Enum):
    UNSET = 0
    CE = 1
    FCC_IC = 2
    RCM = 3


class ResponseType(Enum):
    """
    There are two main response types from the DUT (device under test).
    """

    STATUS = 0
    """Status of the last command (e.g., setup, start tx, start rx, or vendor specific)"""
    PACKET_REPORT = 1
    """The status of the the last end test command contains a 15-bit packet count"""


class ResponseStatus(Enum):
    """
    1-bit status (success or failure).
    """

    SUCCESS = 0
    FAILURE = 1


class VendorSpecific(Enum):
    """
    The length field of a command indicates the vendor specific command type.

    Some are specific to the  nRF5340 + nRF21540.
    """

    CARRIER_TEST = 0
    CARRIER_TEST_STUDIO = 1
    SET_TX_POWER = 2
    FEM_ANTENNA_SELECT = 3
    FEM_GAIN_SET = 4
    FEM_ACTIVE_DELAY_SET = 5
    FEM_DEFAULT_PARAMS_SET = 6


# Packet type is used to indicate a Vendor Specific [sub]command
class PacketType(Enum):
    PRBS9 = 0
    B_11110000 = 1
    B_10101010 = 2
    VS = 3


class CommandBits(ctypes.LittleEndianStructure):
    """
    Structure of the 16-bit command.
    """

    _fields_ = [
        ("pkt", uint16_t, 2),
        ("length", uint16_t, 6),
        ("freq", uint16_t, 6),
        ("cmd", uint16_t, 2),
    ]


class AltTestSetupBits(ctypes.LittleEndianStructure):
    """
    Alternative structure of the 16-bit command.

    For some test setup commands, the packet and length fields
    are combined into a parameter field.
    """

    _fields_ = [
        ("param", uint16_t, 8),
        ("freq", uint16_t, 6),
        ("cmd", uint16_t, 2),
    ]


class ResponseBits(ctypes.LittleEndianStructure):
    """
    Generic structure of a 16-bit response.
    """

    _fields_ = [
        ("data", uint16_t, 15),
        ("ev", uint16_t, 1),
    ]


class StatusEventBits(ctypes.LittleEndianStructure):
    """
    Status response structure.
    """

    _fields_ = [
        ("st", uint16_t, 1),  # status
        ("do_not_care", uint16_t, 14),
        ("ev", uint16_t, 1),
    ]


class PacketReportEventBits(ctypes.LittleEndianStructure):
    """
    Packet response structure.
    """

    _fields_ = [
        ("packet_count", uint16_t, 15),
        ("ev", uint16_t, 1),
    ]


class Command(ctypes.Union):
    """
    A union is used to simplify transporting messages to the DUT.
    """

    _anonymous_ = ("bits",)
    _fields_ = [
        ("bits", CommandBits),
        ("word", uint16_t),
        ("alt", AltTestSetupBits),
    ]


class Response(ctypes.Union):
    """
    A union is used to simplify response handling.
    """

    _anonymous_ = ("bits",)
    _fields_ = [
        ("bits", ResponseBits),
        ("word", uint16_t),
        ("status", StatusEventBits),
        ("report", PacketReportEventBits),
    ]


class DTM:
    """
    A class to represent Direct Test Mode (DTM) for a Device Under Test (DUT).

    Currently, only a UART (serial port) transport is supported.
    All commands are 16 bits in length.

    Unlike the nRF PC DTM application, the reset command and radio configuration
    are not sent each time a test is started.
    """

    def __init__(self, com_port: str):
        """
        Open serial port to device under test.

        Send the reset command.

        Set the packet length to the maximum (and send vendor specific command).
        This is done so that RF power measurements are more accurate with inexpensive spectrum
        analyzers. In addition, most conformance testers use the maximum packet length.

        :param str com_port: Communication port
        :raises Exception: if port cannot be opened or
            reset and packet length commands cannot be sent
        """
        self.test = Command(
            cmd=CommandType.TX.value,
            freq=CHANNEL_MIN,
            length=PACKET_LENGTH_LOWER_MAX,
            pkt=PacketType.PRBS9.value,
        )
        self.packet_count = 0
        self.packet_length = PACKET_LENGTH_MAX
        self.phy = Phy.PHY_1M
        self.antenna = Antenna.EXTERNAL
        self.region = Region.UNSET
        try:
            self.transport = serial.Serial(
                com_port, BAUD_RATE, timeout=SERIAL_TIMEOUT_SECONDS
            )
            self.reset_cmd()
            self.set_packet_length(self.packet_length)
        except:
            raise Exception("Device communication error")

    def __del__(self):
        try:
            self.transport.close()
            del self.transport
        except:
            pass

    def _expect_success(self):
        """
        An error response often indicates that a command was invalid for the current state
        of the DUT.
        """
        b, rsp = self._read()
        if len(b) == 0:
            raise Exception("Response not received")
        elif rsp.bits.ev != ResponseType.STATUS.value:
            logger.error("Response type was not status (it was packet)")
        elif rsp.status.st != ResponseStatus.SUCCESS.value:
            logger.error("Command Failed")

    def _expect_packet_count(self):
        """
        The test end command should return the number of packets.
        """
        b, rsp = self._read()
        if len(b) == 0:
            raise Exception("Response not received")
        elif rsp.bits.ev == ResponseType.PACKET_REPORT.value:
            # Value isn't valid for transmit test (always 0)
            if self.test.cmd == CommandType.RX.value:
                logging.info(
                    f"End Test packet count {rsp.report.packet_count}")
                self.packet_count = rsp.report.packet_count
            else:
                logging.debug("End Test OK")
        elif rsp.status.st != ResponseStatus.SUCCESS.value:
            logger.error("End Test Failed")
        else:
            logger.error("Unexpected response for End Test")

    def _read(self):
        """
        Use transport to read command response from DUT.
        """
        b = self.transport.read(RESPONSE_SIZE)
        rsp = Response(word=int.from_bytes(b, "big"))
        logging.debug(f"Rx {b.hex()}")
        return b, rsp

    def _send_cmd(self, cmd: Command, expect_packet: bool = False):
        """
        Use transport to send a message to the DUT.
        """
        b = cmd.word.to_bytes(2)
        logging.debug(f"Tx {b.hex()}")
        self.transport.write(b)
        self.packet_count = -1
        if expect_packet:
            self._expect_packet_count()
        else:
            self._expect_success()

    def reset_cmd(self):
        """
        Send a reset (test setup) command and expect success.

        Reset the upper bits of the length and set the PHY to 1M.
        """
        self._send_cmd(
            Command(
                cmd=CommandType.TEST_SETUP.value,
                freq=TestSetup.RESET.value,
            )
        )

    def end_test(self):
        """
        Send an end test command and expect a packet response.
        """
        self._send_cmd(Command(cmd=CommandType.END.value), True)

    def start_tx_test(self, freq=None, duration=0.0):
        """
        Start transmit test.

        :param freq: If present, frequency in MHz (2402-2480) to use for test
        :param duration: If greater than 0, the duration of the test in seconds
        """
        logger.debug("Starting TX Test")
        self.test.cmd = CommandType.TX.value
        if freq is not None:
            self.set_frequency(freq)
        self._adjust_power_for_region_and_antenna()
        self._send_cmd(self.test)
        if duration > 0:
            time.sleep(duration)
            self.end_test()
            # Estimate number of packets sent
            # This doesn't take into account the time to send serial messages or
            # execution time.
            self.packet_count = int(
                (duration * 1e6) / self._packet_interval_us())
            logging.info(
                f"Approximately {self.packet_count} packets of {self.packet_length}"
                f"bytes were sent using {self.phy.name}"
            )

    def start_tx_sweep(self, duration=1.0, repeat_count: int = 0):
        """
        Transmit on all channels for duration in seconds.

        :param duration: time to remain on each channel
        :param int repeat_count: Number of times to repeat sweep
        """
        logger.debug("Starting TX Sweep")
        self.test.cmd = CommandType.TX.value
        for _ in range(-1, repeat_count):
            for channel in range(CHANNEL_MIN, CHANNEL_MAX):
                self.test.freq = channel
                self._adjust_power_for_region_and_antenna()
                self._send_cmd(self.test)
                time.sleep(duration)
                self.end_test()

    def start_rx_test(self, freq=None, duration=0.0):
        """
        Start receive test.

        :param freq: If present, frequency in MHz (2402-2480) to use for test
        :param duration: If greater than 0, the duration of the test in seconds
        """
        logger.debug("Starting RX Test")
        self.test.cmd = CommandType.RX.value
        if freq is not None:
            self.set_frequency(freq)
        self._send_cmd(self.test)
        if duration > 0:
            time.sleep(duration)
            self.end_test()

    def set_frequency(self, freq: int):
        """
        Set frequency in MHz (2402 to 2408).
        """
        if (freq % 2) != 0 or freq > FREQ_MAX or freq < FREQ_MIN:
            logger.error("Frequency must be even and 2402 <= freq <= 2480 MHz")
        else:
            self.set_channel_physical((int)((freq - FREQ_MIN) / 2))

    def set_channel_physical(self, channel: int):
        """
        Set physical channel (2*channel + 2402) MHz.\n
        2402 = 0\n
        ...\n
        2440 = 19\n
        ...\n
        2480 = 39
        """
        if channel > CHANNEL_MAX or channel < CHANNEL_MIN:
            logger.error("Invalid channel")
            return
        if self.test.freq != channel:
            self.test.freq = channel
            logger.info(f"Physical channel set to {self.test.freq}")

    def set_channel_logical(self, channel: int):
        """
        Set logical channel.\n
        2402 = 37\n
        2404 = 0\n
        ...\n
        2424 = 10\n
        2426 = 38\n
        2428 = 11\n
        ...\n
        2480 = 39\n
        """
        if channel == 37:
            c = 0
        elif channel == 38:
            c = 12
        elif channel == 39:
            c = 39
        elif channel <= 10:
            c = channel + 1
        else:
            c = channel + 2
        self.set_channel_physical(c)

    def get_channel_logical(self):
        """
        Get logical channel from physical channel.\n
        2402 = 37\n
        2404 = 0\n
        ...\n
        2424 = 10\n
        2426 = 38\n
        2428 = 11\n
        ...\n
        2480 = 39\n
        """
        if self.test.freq == 0:
            return 37
        elif self.test.freq == 12:
            return 38
        elif self.test.freq == 39:
            return 39
        elif self.test.freq <= 11:
            return self.test.freq - 1
        else:
            return self.test.freq - 2

    def _send_vs_cmd(self, sub_cmd: VendorSpecific, param: int):
        """
        Utility for sending a vendor specific command

        :param int param: Frequency field is used to send command parameters
        """
        logger.debug(f"Sending Vendor Specific command: {sub_cmd.name}")
        vendor_specific = Command(
            cmd=CommandType.TX.value,
            freq=param,
            length=sub_cmd.value,
            pkt=PacketType.VS.value,
        )
        self._send_cmd(vendor_specific)

    def tx_constant_carrier(self, freq=None, duration=0.0):
        """
        Start a constant carrier test.

        :param freq: If present, frequency in MHz (2402-2480) to use for test
        :param duration: If greater than 0, the duration of the test in seconds
        """
        if freq is not None:
            self.set_frequency(freq)
        self._send_vs_cmd(VendorSpecific.CARRIER_TEST, self.test.freq)
        if duration > 0:
            time.sleep(duration)
            self.end_test()

    def set_tx_power(self, power: int):
        """
        Set the transmit power using a vendor specific command.

        Power cannot be set while a test is running.

        :param int power: Only set powers supported by the nRF5340
            (:py:data:`NRF5340_SOC_PWR_TABLE`) can be set by the vendor specific command
        """
        if self.region == Region.UNSET:
            self._set_tx_power(power)
        else:
            logging.error("Power cannot be set manually when a region is set")

    def _set_tx_power(self, power: int):
        if power in NRF5340_SOC_PWR_TABLE:
            self._send_vs_cmd(VendorSpecific.SET_TX_POWER, power)
        else:
            logger.error("Invalid SoC output power")

    def _antenna_select(self, ant: int):
        """
        Select the antenna output of the FEM.

        Currently not supported by BL5340PA [PROD-854].

        :param int ant: 2 for antenna 2, else antenna 1
        """
        if ant == 2:
            antenna = 1
        else:
            antenna = 0

        self._send_vs_cmd(VendorSpecific.FEM_ANTENNA_SELECT, antenna)

    def set_fem_gain(self, gain: int):
        """
        Set the gain register of the FEM.\n
        24-26 is nominally 20 dB (20 dBm at the output with SoC output of 0 dBm).\n

        :param int gain: Value of gain register in nRF21540 (0-31)
        """
        if gain < 32 and gain > 0:
            self._send_vs_cmd(VendorSpecific.FEM_GAIN_SET, gain)
        else:
            logger.error("Invalid FEM gain")

    def region_unset(self):
        """
        FEM gain is not kept track of by this module.
        Therefore, it is not possible to change the region without resetting board
        and creating a new object.
        """
        if self.region != Region.UNSET:
            logging.error("Region already set - reset board to set new region")
            return False
        else:
            return True

    def configure_for_ce(self):
        """
        Configure the BL5340PA (nRF5340 output power and FEM gain)
        for operation in Europe (CE).
        """
        if self.region_unset():
            self.region = Region.CE
            self._set_tx_power(-16)
            # Gain of ~18 dB
            self.set_fem_gain(23)

    def configure_for_north_america(self, internal_antenna: bool = False):
        """
        Use FCC/IC power tables.

        Antenna input of FEM cannot be changed during runtime, but its value
        must be known to select the correct power table.
        """
        if self.region_unset():
            self.region = Region.FCC_IC
            if internal_antenna:
                self.antenna = Antenna.INTERNAL

    def configure_for_australia_nz(self, internal_antenna: bool = False):
        """
        Use RCM power tables.

        Antenna input of FEM cannot be changed during runtime, but its value
        must be known to select the correct power table.
        """
        if self.region_unset():
            self.region = Region.RCM
            if internal_antenna:
                self.antenna = Antenna.INTERNAL

    def _adjust_power_for_region_and_antenna(self):
        """
        If required, adjust the transmit power for the region and antenna type.

        The current tables don't require floor/ceiling adjustments to map to
        valid nRF5340 output power levels.
        """
        if self.region == Region.FCC_IC or self.region == Region.RCM:
            self._set_tx_power(
                POWER_TABLE[self.region.name][self.antenna.name][self.phy.name][
                    self.get_channel_logical()
                ]
            )

    def _send_test_setup_cmd(self, sub_cmd: TestSetup, param: int):
        """
        Send a test setup command.
        (e.g., reset, upper length, PHY, modulation, transmit power)
        """
        ts = Command(
            cmd=CommandType.TEST_SETUP.value,
            freq=sub_cmd.value,
            length=param,
            pkt=0,
        )
        if sub_cmd == TestSetup.SET_PHY:
            ts.alt.param = param
        elif param > COMMAND_FREQ_OR_LEN_MAX:
            logger.error("Parameter too large")
            return

        self._send_cmd(ts)

    def _set_phy(self, param: Phy):
        """
        Set the PHY.
        """
        self.phy = param
        self._send_test_setup_cmd(TestSetup.SET_PHY, param.value)

    def set_phy_1M(self):
        """
        Set physical layer to 1 Megabit/second (1 symbol per bit).
        """
        self._set_phy(Phy.PHY_1M)

    def set_phy_2M(self):
        """
        Set physical layer to 2 Megabits/second.
        """
        self._set_phy(Phy.PHY_2M)

    def set_phy_coded_s8(self):
        """
        Set physical layer to coded(8 symbols per bit)
        """
        self._set_phy(Phy.CODED_PHY_S8)

    def set_phy_coded_s2(self):
        """
        Set physical layer to coded(2 symbols per bit)
        """
        self._set_phy(Phy.CODED_PHY_S2)

    def set_packet_length(self, length: int):
        """
        Set the packet length.

        Splits length into two parts.

        Sends the test setup command to set the upper 2 bits of the length.
        The lower part (6 bits) is sent as part of the start test command.

        :param int length: The length of the packet (0-255)
        """
        if length > PACKET_LENGTH_MAX:
            logger.error("Packet length too large")
            return

        upper = (length >> 6) & PACKET_LENGTH_UPPER_MAX
        self.test.length = lower = length & PACKET_LENGTH_LOWER_MAX
        self._send_test_setup_cmd(TestSetup.SET_UPPER, upper)
        self.packet_length = length

    def _packet_interval_us(self):
        """
        Estimate the time per packet in microseconds.

        Modified from dtm.c in NCS 2.4.1

        Copyright (c) 2020 Nordic Semiconductor ASA
        SPDX-License-Identifier: LicenseRef-Nordic-5-Clause
        """
        # Packet overhead
        # see BLE [Vol 6, Part F] page 213
        # 4.1 LE TEST PACKET FORMAT
        overhead = 0
        if self.phy == Phy.PHY_2M:
            # 16 preamble
            # 32 sync word
            #  8 PDU header, actually packetHeaderS0len * 8
            #  8 PDU length, actually packetHeaderLFlen
            # 24 CRC
            overhead = 88  # 11 bytes
        elif self.phy == Phy.PHY_1M:
            #  8 preamble
            # 32 sync word
            #  8 PDU header, actually packetHeaderS0len * 8
            #  8 PDU length, actually packetHeaderLFlen
            # 24 CRC
            overhead = 80  # 10 bytes
        elif self.phy == Phy.CODED_PHY_S8:
            # 80     preamble
            # 32 * 8 sync word coding=8
            #  2 * 8 Coding indicator, coding=8
            #  3 * 8 TERM1 coding=8
            #  8 * 8 PDU header, actually packetHeaderS0len * 8 coding=8
            #  8 * 8 PDU length, actually packetHeaderLFlen coding=8
            # 24 * 8 CRC coding=8
            #  3 * 8 TERM2 coding=8
            overhead = 720  # 90 bytes
        elif self.phy == Phy.CODED_PHY_S2:
            # 80     preamble
            # 32 * 8 sync word coding=8
            #  2 * 8 Coding indicator, coding=8
            #  3 * 8 TERM 1 coding=8
            #  8 * 2 PDU header, actually packetHeaderS0len * 8 coding=2
            #  8 * 2 PDU length, actually packetHeaderLFlen coding=2
            # 24 * 2 CRC coding=2
            #  3 * 2 TERM2 coding=2
            # NOTE: this makes us clock out 46 bits for CI + TERM1 + TERM2
            #       assumption the radio will handle this
            overhead = 462  # 57.75 bytes

        # At 1 MBit/s each bit is a microsecond
        length_us = self.packet_length * 8

        # Account for the encoding of PDU
        if self.phy == Phy.CODED_PHY_S8:
            length_us *= 8  # 1 to 8 encoding
        elif self.phy == Phy.CODED_PHY_S2:
            length_us *= 2  # 1 to 2 encoding

        length_us += overhead

        # Handle double speed
        if self.phy == Phy.PHY_2M:
            length_us = int(length_us / 2)

        packet_interval_us = int(math.ceil((length_us + 249) / 625) * 625)
        logging.info(f"Packet length:   {length_us} microseconds")
        logging.info(f"Packet interval: {packet_interval_us} microseconds")

        return packet_interval_us

    def _set_packet_type(self, pt: PacketType):
        """
        Set the packet type.
        """
        self.test.pkt = pt.value

    def set_packet_type_PRBS9(self):
        """
        Set packet type to pseudorandom binary sequence.
        """
        self._set_packet_type(PacketType.PRBS9)

    def set_packet_type_11110000(self):
        """
        Set packet type to 11110000.
        """
        self._set_packet_type(PacketType.B_11110000)

    def set_packet_type_10101010(self):
        """
        Set packet type to 10101010.
        """
        self._set_packet_type(PacketType.B_10101010)


# To increase verbosity, the level can be set to DEBUG.
if __name__ == "__main__":
    script_name = __file__
    log_file_name = script_name.replace(".py", ".log")
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.FileHandler(log_file_name), logging.StreamHandler()],
    )
