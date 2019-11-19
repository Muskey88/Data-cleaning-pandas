def test_drop_row_26():
    assert remove_rows_with_null(df, 26).shape[0] == 4719
