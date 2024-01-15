import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

source_file = "../0035/data/DEOK_hourly.csv"
names = ["read_dt", "read_mw"]
is_summer = "read_dt >= '2012-05-01' and read_dt < '2012-08-31'"
df = (pd.read_csv(source_file, header=0, names=names,
        parse_dates=['read_dt'])
    .set_index("read_dt")
    .query(is_summer)
    .sort_values("read_dt"))

n_periods = 24
model = ExponentialSmoothing(df.read_mw,
    seasonal='add', seasonal_periods=24, freq="H")
model = model.fit()
forecast = model.forecast(steps=n_periods)

plt.figure(figsize=(10, 6))
plt.plot(df.index[-(7*24):], df.read_mw[-(7*24):])
plt.plot(forecast.index, forecast,
    label='Forecast', color='red')
plt.title('Holt-Winters Exponential Smoothing Forecast')
plt.savefig("forecast.png")
