def test_timestamp_object():
    assert df['LAST_UPDATE_YEAR'][4] == pd.Timestamp('2002-09-01 00:00:00')
