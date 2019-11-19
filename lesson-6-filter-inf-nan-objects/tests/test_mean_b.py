def test_mean_b():
    b = np.array([100, 200, 300, np.inf, np.nan, 400])

    assert(mean_of_array(arr=b)) == 250
