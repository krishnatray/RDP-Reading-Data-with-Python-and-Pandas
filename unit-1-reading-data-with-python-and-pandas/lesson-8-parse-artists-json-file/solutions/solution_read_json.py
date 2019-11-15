import numpy as np
import pandas as pd

artists = pd.read_json('artists.json')

artists.drop(['bio'], axis='columns', inplace=True)

artists.set_index('name', inplace=True)

artists.to_csv('artists.csv')
