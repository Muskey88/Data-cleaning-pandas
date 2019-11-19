import numpy as np
import pandas as pd

def how_many_missing_per_column(dframe):
    return dframe.isna().sum()
