import numpy as np
import pandas as pd
import pyarrow.parquet as pq
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout


def gen_samples(df, cols, var, window=24*7, shift=24):
    buffer = window + shift
    for i in range(len(df)-buffer):
        x = df.iloc[i:i+window][cols]
        y = df.iloc[i+window : i+buffer][var]
        yield x, y


site = 'DEOK'
years = (2016, 2017)
src = pq.read_table("data/data.parquet").to_pandas()

df = src[src.site == site]
df = pd.melt(df, 
    id_vars = ["read_date"],
    value_vars = [f"hour{i:02}" for i in range(24)],
    var_name = "hour",
    value_name = "value")

df["hour"] = df.hour.str.extract('(\d+)', expand=False) + ":00:00"
df['read_dt'] = pd.to_datetime(df.read_date.astype(str) + ' ' + df.hour)
df["dayofweek"] = df.read_dt.dt.dayofweek
df["month"] = df.read_dt.dt.month
df['epoch'] = df.read_dt.astype("int64") // 1e9
df = df[["read_dt", "epoch", "month", "dayofweek", "value"]]
df = df.dropna()
df = df.sort_values('epoch').reset_index(drop=True)

features = ['read_dt', 'month', 'dayofweek', 'value']
predictor = "value"
split_point = df.read_dt.max() - pd.Timedelta(hours=23)
dayahead = df[df.read_dt >= split_point]
train = df[df.read_dt < split_point]
train = gen_samples(train, features, predictor)




model = Sequential()
model.add(LSTM(64, input_shape=(24*7, 3)))
model.add(Dropout(0.2))
model.add(Dense(1))
model.compile(loss='mse', optimizer='adam')

# Train the model
model.fit(train, epochs=5, batch_size=32)


