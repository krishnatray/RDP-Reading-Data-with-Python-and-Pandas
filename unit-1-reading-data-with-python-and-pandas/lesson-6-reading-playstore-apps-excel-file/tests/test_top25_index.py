def test_top25_index():
    assert playstore_df.iloc[23]['App'] == 'Ulta Beauty'
    assert playstore_df.iloc[1]['App'] == 'CDL Practice Test 2018 Edition'
