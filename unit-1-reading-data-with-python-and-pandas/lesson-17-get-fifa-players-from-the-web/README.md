# Get FIFA players from the web

Your task:

- Read and store in a `fifa_df` DataFrame the HTML table found in the `fifa_players.html` file that contains the top 30 FIFA players as of Oct. 30, 2019. The `fifa_players.html` file is a dump generated from this URL: https://www.fifaindex.com/players/top/fifa20_363/
- Remove the first two columns and the last one from the resulting `fifa_df` DataFrame, as they are `Unnamed` and filled with `NaN` objects.
- Create a `most_hits_player` variable containing the player with the most amount of `Hits`.
