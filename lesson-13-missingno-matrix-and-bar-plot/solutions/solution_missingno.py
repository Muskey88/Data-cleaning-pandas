import numpy as np
import pandas as pd
import missingno as msno

def missing_values_plot(dframe):
    return msno.matrix(dframe)

def missing_column_values_plot(dframe):
    return msno.bar(dframe)
