import pandas as pd

data = {'Nama': ['Alice', 'Bob', 'Charlie'], 'Usia': [25, 30, 35]}
df = pd.DataFrame(data)

print(df)
print(df['Nama'])
