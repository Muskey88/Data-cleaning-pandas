import numpy as np
import pandas as pd

def if_columns_have_nan(dframe):
    return dframe.isna().any()
