import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_pacf
from prophet import Prophet
import matplotlib.pyplot as plt

names = ["read_dt", "read_mw"]
is_summer = "read_dt >= '2012-05-01' and read_dt < '2012-08-31'"
df = (pd
    .read_csv("data/utilities/DEOK_hourly.csv", 
        header=0,
        names=names,
        parse_dates=['read_dt'])
    .query(is_summer)
    .sort_values("read_dt")
    .reset_index(drop=True))


# Arima Model
arima = ARIMA(df.set_index("read_dt"), order=(1,0,1),
    seasonal_order=(1, 0, 0, 24)).fit()
forecasts = arima.forecast(steps=24)


plt.figure(figsize=(12, 6))
plot_pacf(df.read_mw, lags=7*24)
plt.axvline(x=24, color='red', linestyle='--')
plt.title('Autocorrelation Function (ACF)')
plt.xlabel('Lag')
plt.ylabel('ACF Value')
plt.grid()
plt.savefig("acf.png")

hist = df[-(24*7):].set_index("read_dt")
plt.figure(figsize=(16, 9))
plt.plot(hist, c="blue")
plt.plot(forecasts, color='red', label='ARIMA Forecast')
plt.title('ARIMA Forecast')
plt.xlabel('Time')
plt.ylabel('Value')
plt.savefig("arima.png")

# Prophet Model
prophet = Prophet()
ts = df.rename(columns={'read_dt': 'ds', 'read_mw': 'y'})
prophet.fit(ts)
future = prophet.make_future_dataframe(periods=24, freq="H")
forecast = prophet.predict(future)

ts = ts[(-24*7):]
hist = forecast[-(24*8):-24]
ds = forecast[-24:]
plt.figure(figsize=(16, 9))
plt.plot(ts.ds, ts.y)
plt.plot(ds.ds, ds.yhat, c='red')
plt.fill_between(ds.ds, ds.yhat_lower, ds.yhat_upper, 
    color='#0072B2', alpha=0.2)
plt.savefig("prophet.png")


# # LSTM NNET Model
# seqlen = 24
# sequences, targets = [], []
# for i in range(len(df) - seqlen):
#     sequences.append(df["read_mw"].iloc[i:i+seqlen].values)
#     targets.append(df["read_mw"].iloc[i+seqlen])

# sequences = np.array(sequences)
# targets = np.array(targets)

# scaler = MinMaxScaler()
# sequences = scaler.fit_transform(sequences)
# targets = scaler.transform(targets.reshape(-1, 1))
# X_train, X_test, y_train, y_test = train_test_split(sequences, targets, test_size=0.2, random_state=42)

# model = (Sequential()
#     .add(LSTM(50, input_shape=(seqlen, 1)))
#     .add(Dense(1))
#     .compile(optimizer='adam', loss='mean_squared_error')
#     .fit(X_train, y_train, epochs=10, batch_size=32))

# forecasts = model.predict(X_test)
# forecasts = scaler.inverse_transform(forecasts)
