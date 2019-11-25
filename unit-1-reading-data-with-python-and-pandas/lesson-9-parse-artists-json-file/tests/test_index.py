def test_index():
    i = pd.Index(['Amedeo Modigliani', 'Vasiliy Kandinskiy', 'Diego Rivera',
              'Claude Monet', 'Rene Magritte'])

    assert artists.index.equals(i)
