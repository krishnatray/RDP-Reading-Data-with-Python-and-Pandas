import numpy as np
import pandas as pd
import requests

dfs = pd.read_html('fifa_players.html', encoding='utf-8')

fifa_df = dfs[0]

fifa_df = fifa_df.iloc[:, 2:-1]

most_hits_player = fifa_df.sort_values('Hits', ascending=False).head(1)
