def test_estimate_solar_output():
    result = estimate_solar_output(28.5, 0.19, 5.5)
    assert result > 9000

def test_roi():
    assert estimate_roi(10000, 1400) == 7.14
