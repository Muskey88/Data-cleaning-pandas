def test_col_0_has_nan():
    assert if_columns_have_nan(df)[0] == True
