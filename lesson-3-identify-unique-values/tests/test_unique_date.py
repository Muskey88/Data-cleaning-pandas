def test_unique_date():
    assert list(identify_unique_values(dataframe=df, column='Date')) == ['September 1, 2018', 'July 7, 2018', 'December 23, 2018',
    'May 16, 2018', 'August 20, 2018', 'November 5, 2018', 'September 13, 2018', 'July 4, 2018', 'October 31, 2018', 'April 9, 2018',
    'March 2, 2018', 'November 15, 2018', 'June 1, 2018', 'January 10, 2018', 'October 11, 2018', 'August 23, 2018', 'May 5, 2018',
    'March 25, 2018', 'July 13, 2018', 'September 6, 2018']
