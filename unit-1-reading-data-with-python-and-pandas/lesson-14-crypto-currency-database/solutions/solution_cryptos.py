import numpy as np
import pandas as pd
import sqlite3

# create a new connection to a db in memory
conn = sqlite3.connect(':memory:')

# create a cursor
c = conn.cursor()

# restore the given cryptos.sql dump
c.executescript(open('cryptos.sql', 'r').read())

crypto_df = pd.read_sql('''SELECT cryptocoins_cryptocurrency.name AS coin_name, cryptocoins_exchange.name AS exchange, symbol, price_usd, percent_change_7d
                            FROM cryptocoins_cryptocurrency
                            JOIN cryptocoins_exchange
                            ON cryptocoins_cryptocurrency.exchange_id = cryptocoins_exchange.id''', conn)

weekly_change_df = crypto_df.sort_values('percent_change_7d', ascending=False)
