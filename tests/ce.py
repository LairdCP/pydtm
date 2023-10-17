try:
    dut = DTM("COM13")
    dut.configure_for_ce()
    dut.start_tx_sweep(duration=1)
except:
    assert False