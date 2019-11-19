def test_unique_rank():
    assert list(identify_unique_values(dataframe=df, column='Rank')) == ['1', nan, '3', '5', '6', '7', '8', '9', '2', '4', 'X', '10']
