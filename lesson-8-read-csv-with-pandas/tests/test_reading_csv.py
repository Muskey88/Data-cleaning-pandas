def test_reading_csv():
    df = reading_csv('movies.csv')

    assert df.iloc[2]['movie_title'] == 'Spectre\xa0'
    assert df.iloc[15]['actor_1_name'] == 'Henry Cavill'
    assert df.iloc[20]['genres'] == 'Adventure|Fantasy'
