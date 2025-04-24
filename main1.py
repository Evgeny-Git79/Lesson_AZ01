import pandas as pd

df = pd.read_csv("dz.csv")
print (df.info())
df.dropna(inplace=True)
print (df.info())
group = df.groupby('City')['Salary'].mean()
print(group)