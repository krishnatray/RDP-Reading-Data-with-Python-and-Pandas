# TSV with The Simpsons episodes

Read and store in a `simpsons` DataFrame the data within the `simpsons-episodes.tsv` TSV (_Tabular Separated Values_) file. This file contains information about all The Simpsons episodes.

Take a look at the file before you read it into a DataFrame and see what will be necessary to parse it correctly.

- Use correct separator as data is tabular separated.
- Use the following `col_names` list as column names.
- Load just `Title`, `Air date`, `Production code` and `IMDB rating`.
- Don't load the first empty columns.
- Set `Production code` as index.
- Null values are encoded as `no_val` values, be careful with that when loading the data.
- Parse the `Air date` columns as Date.
