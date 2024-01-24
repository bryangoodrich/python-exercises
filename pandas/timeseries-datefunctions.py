# 🐍 Daily Pandas 🐼
#
# Time series can be a pain, especially when it comes to these main features
#
# 1️⃣ Handling date and datetime parsing
# 2️⃣ Creating time series sequences
# 3️⃣ Handling time zone and tz transformations
#
# No more jumping between datetime, timedelta, and relativedate, oh my! Pandas does it all with very little effort and you don't need to remember the syntax of this or that library. 
#
# #datanalytics #datascience #dataengineering #machinelearning #devops
# 
# ------
# 🗣 If you like this post, follow Bryan for daily #python tips, and hit that like button so the algorithms help others see it, too. 
# 
# For full code and data on this and other exercises, see https://www.github.com/bryangoodrich/python-exercises
# ------
import datetime
import numpy as np
import pandas as pd

dt = pd.to_datetime(["1/1/2018", np.datetime64("2019-01-01"), datetime.datetime(2020, 1, 1)])
# DatetimeIndex(['2018-01-01', '2019-01-01', '2020-01-01'], dtype='datetime64[ns]', freq=None)

dt = pd.date_range("2023-01-01", periods=24, freq="h")
# DatetimeIndex(['2023-01-01 00:00:00', '2023-01-01 01:00:00',
#                '2023-01-01 02:00:00', '2023-01-01 03:00:00',
#                ...
#                '2023-01-01 20:00:00', '2023-01-01 21:00:00',
#                '2023-01-01 22:00:00', '2023-01-01 23:00:00'],
#               dtype='datetime64[ns]', freq='H')

dt = dt.tz_localize("US/Pacific")
#DatetimeIndex([...], dtype='datetime64[ns, US/Pacific]', freq=None)
dt.tz_convert("UTC")
#DatetimeIndex([...], dtype='datetime64[ns, UTC]', freq=None)



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
# #datanalytics #datascience #dataengineering #machinelearning #devops
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




# 🐍 Daily Pandas 🐼
#
# Offsets. Pandas has a lot of them! I don't even know where to begin.
#
# Let's pick a recent date, you can pull out it's name, we can even offset it by business days. That can useful!
#
# We can use Relativedelta offsets to add/subtract a month or hour or whatever you're looking to do.
#
# More interestingly, these objects have encapsulated information we can access, such as by kwd (keyword) dictionaries.
#
# One such strange one is the FY5253 offset?? Is this some standared fiscal year I'm unawares? I'll be digging into this more! But look at the kwd representation of this offset. I'm excited to learn more!
# 
# #datanalytics #datascience #dataengineering #machinelearning #devops
# 
# ------
# 🗣 If you like this post, follow Bryan for daily #python tips, and hit that like button so the algorithms help others see it, too. 
#
# 💻 For full code and data on this and other exercises, see https://www.github.com/bryangoodrich/python-exercises
# ------

import pandas as pd
from pandas.tseries.offsets import DateOffset

dt = pd.Timestamp("2024-01-15")
dt.day_name()  # Monday
for i in range(1, 10):
    offset = pd.offsets.BDay(i)
    print(f"{(dt+offset).day_name()} {dt+offset}")
# Tuesday   2024-01-16 00:00:00
# Wednesday 2024-01-17 00:00:00
# Thursday  2024-01-18 00:00:00
# Friday    2024-01-19 00:00:00
# Monday    2024-01-22 00:00:00
# ...

offset = DateOffset(months=3)  # Think Wrapper for RelativeDelta
print(dt - offset)
# 2023-10-15 00:00:00

offset = DateOffset(hour=8)
print(dt + offset)
# 2024-01-15 08:00:00

# Stranger!
print(offset.kwds)
# {'hour': 8}

pd.offsets.FY5253Quarter().kwds
# {'weekday': 0,
#  'startingMonth': 1,
#  'qtr_with_extra_week': 1,
#  'variation': 'nearest'}



# 🐍 Daily Pandas 🐼
#
# 
# 
# #datanalytics #datascience #dataengineering #machinelearning #devops
# 
# ------
# 🗣 If you like this post, follow Bryan for daily #python tips, and hit that like button so the algorithms help others see it, too. 
#
# 💻 For full code and data on this and other exercises, see https://www.github.com/bryangoodrich/python-exercises
# ------


