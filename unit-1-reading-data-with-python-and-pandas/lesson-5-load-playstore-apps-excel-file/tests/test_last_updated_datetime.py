def test_last_updated_datetime():
    assert playstore_df['Last_Updated'].dtype == np.dtype('<datetime64[ns]')
