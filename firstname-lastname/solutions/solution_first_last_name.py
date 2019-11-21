import numpy as np
import pandas as pd

df = pd.read_csv('2019-stats.csv')

df = df['2019-stats'].str.split('_', expand=True)

df[['Frist name', 'Last name']] = df.iloc[:, 0].str.split('-', expand=True)

df.drop(columns=0, inplace=True)

df.columns = ['Salary', 'Country', 'Sex', 'First name', 'Last name']
