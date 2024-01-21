# 🐍 Daily Pandas 🐼
#
# Continuing the time series theme, we can create ourselves a simple week of random data and look at different resampling methods to both downsample and upsample.
#
# Specifically, I first aggregate to every 2 hours by taking the mean of 0 and 1, 2 and 3, and so on. You could do the max or sum or even custom aggregates at this point.
#
# With upsampling, I can request a frequency like every 15-minutes and while the gaps off-hour will be NaNs, we can choose a number of ways to fill those gaps, such as fillna, forward fill, backfill, use the nearest value, or interpolate.
#
# It is really impressive how easy it is to do this. I'll continue exploring these time series features built into Pandas tomorrow!
#
# ------
# 🗣 If you like this post, follow Bryan for daily #python tips, and hit that like button so the algorithms help others see it, too. 
# 
# For full code and data on this and other exercises, see https://www.github.com/bryangoodrich/python-exercises
# ------
import numpy as np
import pandas as pd

dt = pd.date_range("2024-01-01", periods=24*7, freq="H")
ts = pd.Series(np.random.randint(0, 100, 24*7), index=dt)
# 2024-01-01 00:00:00    46
# 2024-01-01 01:00:00    32
# 2024-01-01 02:00:00    60
# 2024-01-01 03:00:00    51
# 2024-01-01 04:00:00    51

ts.resample("2h").mean()  # or sum, max, ...
# 2024-01-01 00:00:00    39.0 <- (46+32)/2
# 2024-01-01 02:00:00    55.5 <- (60+51)/2
# 2024-01-01 04:00:00    31.5 <- (51+12)/2
# 2024-01-01 06:00:00    49.5 ...
# 2024-01-01 08:00:00    71.0 ...

ts.resample("15min").asfreq()
# 2024-01-01 00:00:00    46.0
# 2024-01-01 00:15:00     NaN
# 2024-01-01 00:30:00     NaN
# 2024-01-01 00:45:00     NaN
# 2024-01-01 01:00:00    32.0

ts.resample("15min").ffill()  # or bfill, nearest, interpolate
# 2024-01-01 00:00:00    46
# 2024-01-01 00:15:00    46
# 2024-01-01 00:30:00    46
# 2024-01-01 00:45:00    46
# 2024-01-01 01:00:00    32
