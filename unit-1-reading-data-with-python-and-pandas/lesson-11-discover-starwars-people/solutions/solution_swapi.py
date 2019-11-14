import numpy as np
import pandas as pd
import requests

# Make a request to SWAPI
req = requests.get('https://swapi.co/api/people/?format=json')

# Parse the request to JSON format
swapi_dict = req.json()

# Create a DataFrame with the JSON data
starwars_people_df = pd.DataFrame.from_dict(swapi_dict['results'])

# Get blue-eyed characters
blue_eyed_people_df = starwars_people_df.loc[starwars_people_df['eye_color'] == 'blue']