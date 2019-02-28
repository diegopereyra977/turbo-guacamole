# !/usr/bin/python3

import pandas as pd


df = pd.read_csv('casas_floresta.csv', sep=';')

print(df.describe(include='all'))
print(df.info())
print(df.head())
