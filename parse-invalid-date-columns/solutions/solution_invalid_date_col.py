import numpy as np
import pandas as pd

df = pd.read_csv('property-data.csv')

df['LAST_UPDATE_YEAR'] = pd.to_datetime(df['LAST_UPDATE_YEAR'])
