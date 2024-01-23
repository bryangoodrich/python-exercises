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
