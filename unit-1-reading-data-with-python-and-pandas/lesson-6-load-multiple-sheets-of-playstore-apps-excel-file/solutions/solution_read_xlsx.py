import numpy as np
import pandas as pd

file = pd.ExcelFile('playstore.xlsx')

playstore_df = file.parse(index_col=0)

content_id_df = file.parse('Content_ID', 
                          index_col='Content_ID')