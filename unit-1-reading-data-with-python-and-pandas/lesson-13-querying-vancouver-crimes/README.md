# Querying Vancouver crimes

- Create a sqlite3 connection to the `van_crimes_2003.db` SQLite3 database.
- Select `TYPE`, `MONTH`, `DAY` and `NEIGHBOURHOOD` from the `van_crimes` table, but only the crime observations from `Stanley Park` or `West End`. Store the information in a `van_crimes_df` DataFrame.
- In a `crime_types_count` variable store the count of crimes per `TYPE`.