import numpy as np
import pandas as pd

data_url = 'https://github.com/ine-rmotr-projects/project-files/files/4086772/playstore.xlsx'

file = pd.ExcelFile(data_url)

playstore_df = file.parse(index_col=0)

content_id_df = file.parse('Content_ID', 
                          index_col='Content_ID')