import numpy as np
import pandas as pd

playstore_df = pd.read_excel('playstore.xlsx',
                   parse_dates=['Last_Updated'],
                   usecols=['App', 'Rating', 'Installs', 'Rating', 'Genres', 'Last_Updated'])

# Filter top 25 rated apps
playstore_df = playstore_df.sort_values('Rating', ascending=False).head(25)
