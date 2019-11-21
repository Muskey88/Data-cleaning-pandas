import numpy as np
import pandas as pd

df = pd.read_csv('property-data.csv')

df['BEDROOMS'] = pd.to_numeric(df['BEDROOMS'], errors='coerce')

df['BATHROOMS'] = pd.to_numeric(df['BATHROOMS'], errors='coerce')

df['SQUARE_FEET'] = pd.to_numeric(df['SQUARE_FEET'], errors='coerce')

df.dropna(inplace=True)
