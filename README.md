# Python Direct Test Mode for Bluetooth

The [pydtm](https://lairdcp.github.io/pydtm/) software module uses the serial port to communicate with an nRF5340 + nRF21540 (BL5340PA) using Direct Test Mode commands as described [here](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/2.6.1/nrf/samples/bluetooth/direct_test_mode/README.html). A visually concise summary for a similar part is [here](https://www.engeniustech.com/technical-papers/BLE-direct-test.pdf).

Unlike the nRF PC DTM application, this doesn't send the test reset command and configuration each time a test is started.

One reason for using this instead of the nRF Connect DTM application is that it allows the gain of the FEM to be modified. This is required to reproduce the testing done for CE compliance. Another reason is that it estimates the number of packets sent during a transmit test of fixed duration.

## Usage

More documentation can be found by opening /docs/index.html.

The examples below show the module being used in interactive mode.

### Transmit test

```
python -i dtm.py
>>> foo = DTM("COM13")
>>> foo.start_rx_test(2402)
>>> foo.start_tx_test(2404)
2023-10-11 16:15:30 Physical channel set to 1
>>> foo.end_test()
```

### Receive Test

Default configuration is 2402 MHz and 1M PHY.

The number of packets transmitted is computed by Python and will most likely be less than the actual number transmitted. This is because of the time required to send the end test message to the transmitter.

```
python -i dtm.py
>>> dut1 = DTM("COM12")
>>> dut2 = DTM("COM13")
>>> dut1.start_rx_test()
>>> dut2.start_tx_test(duration=2)
11:07:56 Packet length:   2120 microseconds
11:07:56 Packet interval: 2500 microseconds
11:07:56 Approximately 800 packets of 255 bytes were sent using PHY_1M
>>> dut1.end_test()
11:07:59 Packet count 804
```

### Configure for CE

This configures the BL5340PA with the settings used for Europe (CE).

```
python -i dtm.py
>>> dut = DTM("COM13")
>>> dut.configure_for_ce()
>>> dut.start_tx_test()
```


