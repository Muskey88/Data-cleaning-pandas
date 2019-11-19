def test_total_nan_name():
    assert(total_nan_values(dataframe=df, column='Name')) == 1
