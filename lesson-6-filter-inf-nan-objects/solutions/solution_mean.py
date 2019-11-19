import numpy as np

def mean_of_array(arr):
    return arr[np.isfinite(arr)].mean()
