def test_float:
    import pandas.api.types as ptypes
    
    assert ptypes.is_float_dtype(df['Salary'])
