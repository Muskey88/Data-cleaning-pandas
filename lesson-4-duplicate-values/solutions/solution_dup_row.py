import numpay as np
import pandas as pd

def duplicate_rows(dframe):
    return dframe[dframe.duplicated()]
