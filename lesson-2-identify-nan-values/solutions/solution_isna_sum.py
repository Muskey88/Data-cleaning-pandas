import numpy as np
import pandas as pd

def total_nan_values(dframe, col):
    return dframe[col].isna().sum()
