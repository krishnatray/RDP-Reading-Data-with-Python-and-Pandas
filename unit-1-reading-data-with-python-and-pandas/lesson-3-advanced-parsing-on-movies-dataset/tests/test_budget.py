def test_budget():
    assert movies.loc[:, 'budget'].min() == 105000000.0
