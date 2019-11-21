def test_empty():
    array = np.array([np.nan, np.inf, np.nan, np.inf, np.nan, np.inf, np.nan, np.inf])

    assert np.array_equal(clean_array(array, clean_inf=True), np.array([]))
