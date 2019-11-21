def test_last_update_year_datetime():
    import pandas.api.types as ptypes
    
    df['LAST_UPDATE_YEAR'] = pd.to_datetime(df['LAST_UPDATE_YEAR'])
