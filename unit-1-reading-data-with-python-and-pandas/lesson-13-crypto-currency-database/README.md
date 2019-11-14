# Crypto currency database

- Create a sqlite3 connection to the `cryptos.db` SQLite3 database. This database contains two tables `cryptocoins_cryptocurrency` and `cryptocoins_exchange`.

- Using `read_sql` method write a query that:
  - Join both tables and return the list of cryptocurrencies with its exchanges. You should use the column with the exchange ID on each table to perform the join.
  - As both tables have a `name` column you should rename `cryptocoins_cryptocurrency.name` as `coin_name` and `cryptocoins_exchange.name` as `exchange`. Also select `symbol`, `price_usd` and `percent_change_7d` columns.
  - Store the information in a `crypto_df` DataFrame.

- Once you have the `crypto_df` DataFrame, create a new `weekly_change_df` with the `crypto_df` data sorted by `percent_change_7d` from highest to lowest.