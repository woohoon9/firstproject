import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.rand(6,4))

print(df)

df.columns = ["A","B","C","D"]
df.index = pd.date_range(start='8/20/2021', periods=6)
print(df.index)

print(df)

df["F"]=[1.0, np.nan, 3.5, 6.1, np.nan, 7.0]
print(df)

df["A"][0:3] = np.nan
print(df)

df.dropna(how='all')
print(df)

df.dropna(axis='columns', how='any')
print(df)
