# Load PlayStore Apps Excel file

Read the `playstore.xlsx` Excel file from the given `data_url` and store it in a `playstore_df` DataFrame.

- When reading in the file, only use the columns `'App', 'Rating', 'Installs', 'Rating', 'Genres', 'Last_Updated'`.
- Make sure `Last_Updated` is in datetime format, try do this while reading the file into the DataFrame.

After reading the data, filter the records and keep only the top 25 with highest `Rating` (being 5 the highest possible rating value).

> This files originated as a CSV from Kaggle and has been altered for this course, https://www.kaggle.com/lava18/google-play-store-apps
