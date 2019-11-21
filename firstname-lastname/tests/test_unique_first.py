def test_unique_first():
    assert df['First name'].unique() == pd.array(['Liam', 'Noah', 'Logan', 'James', 'Oliver', 'Emma',
                                                  'Ava', 'Olivia', 'Isabella', 'Amelia'], dtype=object)
