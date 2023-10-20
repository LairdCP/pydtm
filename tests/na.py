try:
    dut = DTM("COM9")
    dut.configure_for_north_america()
    dut.start_tx_sweep()
    dut.start_tx_test(2440)
    dut.end_test()
except:
    assert False

# manual tests
# ensure power level is correct for region
# ensure tx power cannot be set when region is set
# ensure region cannot be set when it is already set
#
