def test_score():
    assert movies.loc[:, 'imdb_score'].max() == 9
