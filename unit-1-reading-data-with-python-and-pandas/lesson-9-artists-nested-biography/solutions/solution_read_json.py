import numpy as np
import pandas as pd
import json
from pandas.io.json import json_normalize

with open('artists.json') as file:
    json_dict = json.load(file)

artists = json_normalize(json_dict)

biography = json_normalize(json_dict,
                           record_path='bio',
                           meta=['name'])