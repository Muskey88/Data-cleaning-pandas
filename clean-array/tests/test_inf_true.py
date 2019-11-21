def test_inf_true():
    array = np.array([10, 35, np.nan, 100, np.nan, np.inf, 85, 99])
    
    assert np.array_equal(clean_array(array, clean_inf=True), np.array([ 10.,  35., 100.,  85.,  99.]))
