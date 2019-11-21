def test_min_salary():
    condition = df['Salary'] == df['Salary'].min()

    assert np.array_equal(df[condition].values,
    np.array([[22750.0, 'IT', 'M', 'James', 'Bouchard']], dtype=object))
