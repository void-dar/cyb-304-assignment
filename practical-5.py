import pandas as pd

data = pd.read_csv("students.csv")
print(data.isnull().sum())
cleaned = data.dropna()
cleaned.to_csv("cleaned.csv", index=False)