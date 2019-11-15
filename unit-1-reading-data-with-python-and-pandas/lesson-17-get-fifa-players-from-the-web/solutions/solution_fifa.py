import numpy as np
import pandas as pd
import requests

req = requests.get('https://www.fifaindex.com/players/top/fifa20_363/')

dfs = pd.read_html(req.text)

fifa_df = dfs[0]

fifa_df = fifa_df.iloc[:, 2:-1]

most_hits_player = fifa_df.sort_values('Hits', ascending=False).head(1)
