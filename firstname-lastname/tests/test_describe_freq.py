def test_describe_freq():
    assert df.describe().loc['freq']['Country'] == 2
