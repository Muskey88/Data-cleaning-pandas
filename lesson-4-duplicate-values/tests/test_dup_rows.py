def test_dup_rows():
    assert_frame_equal(duplicate_rows(df).set_index('Name'),
    pd.DataFrame([['F',	'Sophia', '104', '3', 'December 23, 2018'], ['M', 'Ryan', '160', '2', 'November 15, 2018']],
    columns=['Gender',	'Name',	'Count',	'Rank',	'Date']).set_index('Name'))
