def test_blue_eyed_people_2():
    assert blue_eyed_people_df.loc[blue_eyed_people_df['gender'] == 'male']['gender'].count()
