import numpy as np
import pandas as pd
import sqlite3

# create a new connection to a db in memory
conn = sqlite3.connect(':memory:')

# create a cursor
c = conn.cursor()

# restore the given cryptos.sql dump
c.executescript(open('cryptos.sql', 'r').read())

# your code goes here
