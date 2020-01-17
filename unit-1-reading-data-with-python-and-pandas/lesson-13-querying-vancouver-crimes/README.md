# Querying Vancouver crimes

Using the given sqlite3 connection:
- Select `TYPE`, `MONTH`, `DAY` and `NEIGHBOURHOOD` from the `van_crimes` table, but only the crime observations from `Stanley Park` or `West End`. Store the information in a `van_crimes_df` DataFrame.
- Store the count of crimes per `TYPE` in a `crime_types_count` variable.