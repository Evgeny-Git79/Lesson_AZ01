import pandas as pd

df = pd.read_csv("Dow_Jones.csv")

print(df.head())
print(df.tail())
print(df.describe())
print(df.info())
