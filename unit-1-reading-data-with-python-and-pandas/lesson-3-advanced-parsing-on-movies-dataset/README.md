# Advanced parsing on movies dataset

Read and store in a `movies` DataFrame the data within the `movies.csv` file.

This assignment will require a few extra steps. We will be using the same `movies.csv` as the previous exercise.

- Use the appropriate separator.
- The given data doesn't have a defined header. Use the column names given in the `column_names` variable.
- Missing values are encoded as `?` characters. Parse those values as `NaN` objects.
- The `budget` column has commas separating the thousands, make sure the column is of float data type.
- The index of the DataFrame should be represented by the `movie_title` column.

> This CSV is altered for this course and originally from Kaggle, https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset
