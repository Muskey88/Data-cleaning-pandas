def test_col_9_has_nan():
    assert if_columns_have_nan(df)[9] == False
