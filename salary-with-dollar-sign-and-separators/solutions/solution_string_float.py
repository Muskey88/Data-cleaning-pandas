import numpy as np
import pandas as pd

df = pd.read_csv('2019-stats-cleaner.csv')

df['Salary'] = df['Salary'].str.replace('$', '')

df['Salary'] = df['Salary'].str.replace('.', '')

df['Salary'] = df['Salary'].str.replace(',', '.')

df['Salary'] = df['Salary'].astype('float')
