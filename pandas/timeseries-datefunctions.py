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
