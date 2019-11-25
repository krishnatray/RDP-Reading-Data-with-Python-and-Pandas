def test_content_id_2():
    content_id_head = pd.DataFrame({'Content_Rating': ['Everyone', 'Everyone', 'Everyone', 'Teen', 'Everyone']},
                                   index=[101, 101, 101, 102, 101])
                                
    assert content_id_df.head().equals(content_id_head)