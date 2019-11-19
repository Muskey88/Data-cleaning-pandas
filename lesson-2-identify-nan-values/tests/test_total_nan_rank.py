def test_total_nan_rank():
    assert(total_nan_values(dataframe=df, column='Rank')) == 3
