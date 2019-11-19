def test_mean_a():
    a = np.array([20, 40, 60, np.nan, np.nan, 80])
    
    assert(mean_of_array(arr=a)) == 50
