import os
import pandas as pd
from pyarrow import Table
from pyarrow.parquet import write_table

def reader(fh):
    site = os.path.splitext(os.path.basename(fh))[0]
    site = site.split("_")[0]
    names = ["read_dt", "read_mw"]
    df = pd.read_csv(fh, header=0, 
        names=names, parse_dates=['read_dt'])
    df['read_date'] = pd.to_datetime(df['read_dt']).dt.date
    df['read_hour'] = df.read_dt.dt.hour
    df['site'] = site
    return df

files = os.listdir("data")
dfs = (reader(os.path.join("data", file)) for file in files)
combined = pd.concat(dfs, ignore_index=True)
combined.drop("read_dt", axis=1, inplace=True)

df = (combined
    .groupby(['site', 'read_date', 'read_hour'])['read_mw']
    .mean()
    .reset_index()
    .pivot(index=['site', 'read_date'],
        columns="read_hour", values='read_mw'))

df.columns = [f'hour{hour:02}' for hour in df.columns]
df = df.reset_index()

write_table(Table.from_pandas(df), 'data.parquet')
