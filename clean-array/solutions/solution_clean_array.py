import numpy as np

def clean_array(arr, clean_inf=False):
    if clean_inf:
        return arr[np.isfinite(arr)]
    return arr[~np.isnan(arr)]
