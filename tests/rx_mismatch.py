#
# Ensure 0 packets are received when settings don't match
#
dut1 = DTM("COM12")
dut2 = DTM("COM13")

# 384 packets
dut1.start_rx_test()
dut2.start_tx_test(duration=1.2)
dut1.end_test()
assert dut1.packet_count >= dut2.packet_count

# 0 packets
dut1.set_phy_1M()
dut1.start_rx_test()
dut2.set_phy_coded_s8()
dut2.start_tx_test(duration=2)
dut1.end_test()
assert dut1.packet_count == 0

# 640
dut1.set_phy_coded_s8()
dut1.start_rx_test()
dut2.set_phy_coded_s8()
dut2.start_tx_test(duration=2)
dut1.end_test()
assert dut1.packet_count >= dut2.packet_count

# 0 packets
dut1.set_phy_2M()
dut1.start_rx_test(freq=2440)
dut2.set_phy_2M()
dut2.start_tx_test(freq=2480, duration=2)
dut1.end_test()
assert dut1.packet_count == 0

# This seems to indicate that setting the packet length on receiver doesn't matter
dut1.set_packet_length(20)
dut2.set_packet_length(64)
dut1.set_phy_2M()
dut1.start_rx_test(freq=2440)
dut2.set_phy_2M()
dut2.start_tx_test(freq=2440, duration=2)
dut1.end_test()
assert dut1.packet_count >= dut2.packet_count
