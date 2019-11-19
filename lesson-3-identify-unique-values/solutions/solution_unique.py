import numpy as np
import pandas as pd

df = pd.read_csv('baby_names.csv')

def identify_unique_values(dframe, col):
    return dframe[col].unique()
