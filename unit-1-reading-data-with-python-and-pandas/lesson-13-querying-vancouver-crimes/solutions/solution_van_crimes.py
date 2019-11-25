import numpy as np
import pandas as pd
import sqlite3

conn = sqlite3.connect('van_crime_2003.db')

van_crimes_df = pd.read_sql('''SELECT TYPE, MONTH, DAY, NEIGHBOURHOOD
                            FROM van_crimes WHERE NEIGHBOURHOOD IN ("Stanley Park", "West End")''', conn)

crime_types_count = van_crimes_df['TYPE'].value_counts()
