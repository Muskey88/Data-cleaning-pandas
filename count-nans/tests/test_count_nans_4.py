def test_count_nans_4():
    array = np.array([np.nan, 1000, np.nan, 350, 1, np.nan, np.nan, 25, 94])

    assert count_nans(array) == 4
