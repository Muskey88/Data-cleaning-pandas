def test_drop_row_22():
    assert remove_rows_with_null(df, 22).shape[0] == 5005
