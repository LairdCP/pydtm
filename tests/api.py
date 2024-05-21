try:
    dut = DTM("COM21")
    dut.reset_cmd()
    # no params
    dut.start_tx_test()
    dut.end_test()
    # no params
    dut.start_rx_test()
    dut.end_test()
    #
    dut.start_tx_sweep(0.2)
    # tx freq and duration
    dut.start_tx_test(2480)
    dut.end_test()
    dut.start_tx_test(2440, duration=1)
    dut.start_tx_test(freq=2402, duration=1.9)
    # rx freq and duration
    dut.start_rx_test(2480)
    dut.end_test()
    dut.start_rx_test(duration=1)
    dut.start_rx_test(freq=2440, duration=2.2)
    #
    dut.tx_constant_carrier()
    dut.end_test()
    dut.tx_constant_carrier(2440, duration=3)
    #
    dut.set_frequency(2408)
    assert dut.test.freq == 3
    dut.set_channel_physical(8)
    assert dut.test.freq == 8
    dut.set_channel_logical(9)
    assert dut.test.freq == 10
    dut.set_channel_logical(37)
    assert dut.test.freq == 0
    dut.set_channel_logical(38)
    assert dut.test.freq == 12
    dut.set_channel_logical(39)
    assert dut.test.freq == 39
    dut.set_channel_logical(10)
    assert dut.test.freq == 11
    dut.set_channel_logical(11)
    assert dut.test.freq == 13
    #
    dut.set_packet_type_PRBS9()
    dut.start_tx_test(duration=0.5)
    dut.set_packet_type_11110000()
    dut.start_tx_test(duration=0.5)
    dut.set_packet_type_10101010()
    dut.start_tx_test(duration=0.5)
    #
except:
    assert False
