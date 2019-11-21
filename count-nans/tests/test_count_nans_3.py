def test_count_nans_3():
    array = np.array([np.nan, np.inf, np.nan, np.nan, np.inf, 1, np.inf])

    assert count_nans(array) == 3
