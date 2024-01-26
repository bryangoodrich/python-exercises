# 🐍 Daily Pandas 🐼
# 
# One thing I really like about Pandas is the built-in time series operations it has. One of those is the diff method you can take on a DataFrame or Series object. Here I pull out the first difference (lag1) and the difference of the difference (lag2). I also pass in 12 to get the difference between each point and 12 points ago, in case there's some 12 hour seasonality in the data. Really, AR would have been a correlation, but this is my stand-in. 
# 
# Do you use time series in Pandas? Tell me your stories! 
# 
# #datanalytics #datascience #dataengineering #machinelearning #devops
# 
# ------
# 🗣 If you like this post, follow Bryan for daily #python tips, and hit that like button so the algorithms help others see it, too. 
# 
# For full code and data on this and other exercises, see https://www.github.com/bryangoodrich/python-exercises
# ------

import pandas as pd
import statsmodels.api as sm

data = sm.datasets.co2.load_pandas().data
data['lag1'] = data.co2.diff()
data['lag2'] = data.co2.diff().diff()
data['ar12'] = data.co2.diff(12)

#               co2  lag1  lag2  ar12
# 1958-03-29  316.1   NaN   NaN   NaN
# 1958-04-05  317.3   1.2   NaN   NaN
# 1958-04-12  317.6   0.3  -0.9   NaN
# 1958-04-19  317.5  -0.1  -0.4   NaN
# 1958-04-26  316.4  -1.1  -1.0   NaN
# ...           ...   ...   ...   ...
# 2001-12-01  370.3   0.0  -0.6   2.1
# 2001-12-08  370.8   0.5   0.5   2.8
# 2001-12-15  371.2   0.4  -0.1   3.8
# 2001-12-22  371.3   0.1  -0.3   3.9
# 2001-12-29  371.5   0.2   0.1   3.7




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
# After seeing how offsets work, I revisited the resampling methods where you can do some strange things.
#
# With the W specifier, we can get weekly resampling (aggregation), but we can also tell it what the start of the week is with W-MON.
#
# But notice I pull the first observed weekday name, which is the Tuesday value, and in the weekly aggregate the date listed is the next Monday!
#
# So in a very important way, the aggregate timestamp is really "as of the end of the period." 
# 
# #datanalytics #datascience #dataengineering #machinelearning #devops
# 
# ------
# 🗣 If you like this post, follow Bryan for daily #python tips, and hit that like button so the algorithms help others see it, too. 
#
# 💻 For full code and data on this and other exercises, see https://www.github.com/bryangoodrich/python-exercises
# ------
# Reference: https://machinelearningtutorials.org/python-pandas-data-offsets-with-examples/

import numpy as np
import pandas as pd

dates = pd.date_range(
    start='2024-01-01',
    end='2024-01-31',
    freq='D')

data = np.random.randint(0, 100, size=len(dates))

df = pd.DataFrame({
    'date': dates, 
    'value': data,
    'weekday': dates.day_name()
})
#          date  value    weekday
# 0  2024-01-01     18     Monday
# 1  2024-01-02     87    Tuesday
# 2  2024-01-03     82  Wednesday
# 3  2024-01-04     83   Thursday
# 4  2024-01-05     41     Friday
# 5  2024-01-06     99   Saturday
# 6  2024-01-07     92     Sunday
# 7  2024-01-08     22     Monday
# 8  2024-01-09     24    Tuesday

aggregation = {"value": "sum", "weekday": "first"}
weekly = df.resample('W', on='date').agg(aggregation).reset_index()
#         date  value  weekday
# 0 2024-01-01     18   Monday
# 1 2024-01-08    506  Tuesday  <- 87+82+83+41+99+92+22
# 2 2024-01-15    370  Tuesday
# 3 2024-01-22    291  Tuesday
# 4 2024-01-29    330  Tuesday
# 5 2024-02-05    140  Tuesday

weekly.date.dt.day_name()  # All Monday!


# 🐍 Daily Pandas 🐼
#
# If you want to customize your time series sequences, you can specify things like "every other Friday" or whatever logic you're trying to capture. You can see it's doing exactly what I asked for leveraging the CustomBusinessDay.
#
# One of the optimizations in Pandas is using the DateTimeIndex. I use this dates series as an index, and you can do partial indexing into your data! For series it's direct, like ts["2024"], but in a DataFrame, we have to use the df.loc[...] syntax. And as you can see, I can filter for a month very naturally. Nice!
#
# #datanalytics #datascience #dataengineering #machinelearning #devops
#
# ------
# 🗣 Follow Bryan for more daily #python tips and smash that like button! 💥
#
# 💻 Full repo https://www.github.com/bryangoodrich/python-exercises 👀
# ------
# Reference: https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html

import pandas as pd

every_other_fri = pd.offsets.CustomBusinessDay(n=2, weekmask='Fri')
dates = pd.date_range('2024-01-01', periods=8, freq=every_other_fri)
pd.DataFrame({"dates": dates, "weekday": dates.day_name()})
# 0 2024-01-05  Friday
# 1 2024-01-19  Friday
# 2 2024-02-02  Friday
# 3 2024-02-16  Friday
# 4 2024-03-01  Friday
# 5 2024-03-15  Friday
# 6 2024-03-29  Friday
# 7 2024-04-12  Friday


df = pd.DataFrame({
    "costs": [100, 200, 300, 400, 500, 600, 700, 800],
    "sales": [39, 945, 183, 93, 10, 394, 65, 73]
}, index=dates)

df.loc["2024-01"]
#             costs  sales
# 2024-01-05    100     39
# 2024-01-19    200    945
