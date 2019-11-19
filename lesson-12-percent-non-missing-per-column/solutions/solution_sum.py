import numpy as np
import pandas as pd

def percent_non_missing_per_column(dframe):
    return (dframe.notnull().sum() / dframe.shape[0]) * 100
