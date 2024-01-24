import os
import pandas as pd

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

data_dir = "data/utilities"
files = os.listdir(data_dir)
dfs = (reader(f"{data_dir}/{file}") for file in files)
batch_data = pd.concat(dfs, ignore_index=True)
batch_data.to_parquet('data/batch_data.parquet')