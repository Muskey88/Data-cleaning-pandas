import numpy as np

def count_nans(arr):
    return np.isnan(arr).sum()
