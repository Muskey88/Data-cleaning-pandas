import numpy as np
import pandas as pd

def drop_columns_with_all_nan(dframe):
    return dframe.dropna(axis='columns', how='all')
