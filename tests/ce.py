try:
    dut = DTM("COM21")
    dut.configure_for_ce()
    dut.start_tx_sweep(duration=1)
except:
    assert False