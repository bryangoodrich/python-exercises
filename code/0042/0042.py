import pandas as pd

df = pd.read_csv("data.csv")
df.columns = df.columns.str.lower()



