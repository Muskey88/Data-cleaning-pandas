def test_drop_tweets():
    assert drop_columns_with_all_nan(df).shape[1] == 28
