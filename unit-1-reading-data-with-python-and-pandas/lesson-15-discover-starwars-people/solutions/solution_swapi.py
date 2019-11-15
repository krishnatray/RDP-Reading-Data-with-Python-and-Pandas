import numpy as np
import pandas as pd
import requests

req = requests.get('https://swapi.co/api/people/?format=json')

swapi_dict = req.json()

starwars_people_df = pd.DataFrame.from_dict(swapi_dict['results'])

blue_eyed_people_df = starwars_people_df.loc[starwars_people_df['eye_color'] == 'blue']
