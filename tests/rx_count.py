#
# Test that received packets are >= sent packets (in an ideal system).
# This [ab]uses the fact that there is an execution/comm delay when running the
# script that results in more packets being sent than the amount computed.
#
dut1 = DTM("COM21")
dut2 = DTM("COM28")

for length in [32, 73, 255]:
    dut1.set_packet_length(length)
    dut2.set_packet_length(length)
    dut1.set_phy_2M()
    dut1.start_rx_test(freq=2440)
    dut2.set_phy_2M()
    dut2.start_tx_test(freq=2440, duration=2)
    dut1.end_test()
    assert dut1.packet_count >= dut2.packet_count
    dut1.set_phy_coded_s2()
    dut1.start_rx_test(freq=2480)
    dut2.set_phy_coded_s2()
    dut2.start_tx_test(freq=2480, duration=2)
    dut1.end_test()
    assert dut1.packet_count >= dut2.packet_count
    dut1.set_phy_1M()
    dut1.start_rx_test(freq=2480)
    dut2.set_phy_1M()
    dut2.start_tx_test(freq=2480, duration=2)
    dut1.end_test()
    assert dut1.packet_count >= dut2.packet_count
    dut1.set_phy_coded_s8()
    dut1.start_rx_test(freq=2402)
    dut2.set_phy_coded_s8()
    dut2.start_tx_test(freq=2402, duration=2)
    dut1.end_test()
    assert dut1.packet_count >= dut2.packet_count
