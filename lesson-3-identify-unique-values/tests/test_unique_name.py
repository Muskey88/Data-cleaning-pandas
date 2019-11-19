def test_unique_name():
    assert list(identify_unique_values(dataframe=df, column='Name')) == ['Olivia', 'chloe', 'Sophia', nan, 'Emma', 'mia', 'Charlotte', 'Sarah',
    'Isabella', 'Han nah', 'Ethan', 'Ryan', 'Muhammad', 'Lucas', 'Jay den', 'Aiden', 'daniel', 'Evan', 'Jason', 'Liam']
