import numpy as np
import pandas as pd

col_names = ['Title', 'Air date', 'Production code', 'Season', 'Number in season',
             'Number in series', 'US viewers (million)', 'Views', 'IMDB rating']

select_cols = ['Title','Air date','Production code','IMDB rating']

simpsons = pd.read_csv('simpsons-episodes.tsv',
                 sep='\t',
                 encoding='UTF-8',
                 names=col_names,
                 usecols=select_cols,
                 skiprows=4,
                 index_col='Production code',
                 na_values=['no_val'],
                 parse_dates=['Air date'])
