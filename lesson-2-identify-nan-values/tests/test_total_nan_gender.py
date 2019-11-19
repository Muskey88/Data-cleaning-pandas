def test_total_nan_gender():
    assert(total_nan_values(dataframe=df, column='Gender')) == 5
