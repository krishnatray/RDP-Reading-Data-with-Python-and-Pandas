import numpy as np
import pandas as pd

data_url = 'https://github.com/ine-rmotr-projects/project-files/files/4086772/playstore.xlsx'

playstore_df = pd.read_excel(data_url,
                   parse_dates=['Last_Updated'],
                   usecols=['App', 'Rating', 'Installs', 'Rating', 'Genres', 'Last_Updated'])

playstore_df = playstore_df.sort_values('Rating', ascending=False).head(25)
