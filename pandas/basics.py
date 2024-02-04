# 🐍 Daily Pandas 🐼
#
# When learning programming, you may encounter that some objects are references to other objects, and this can cause some issues. With Pandas, they're introducing a new default behavior in 3.0 called Copy on Write (CoW).
# 
# Suppose you reference a subset (column) of your DataFrame df, like my df.grades example. In this example, today's behavior is I could just replace a value like the first grade from 98 --> 88. 
# 
# If we turn copy_on_write option to True, we change the subset but not the original df. How? 🙋
# 
# The idea if the subset originally was just a reference to the column series in the original DataFrame. However, when we attempted to write/change this reference, Pandas will now make a new copy of the Series for you to alter, instead, breaking the reference linkage and protecting the original object. Immutabilty matters! 🤔
# 
# With CoW on, we get an error when trying to replace this through a secondary assignment like in the df.grades.replace(...) syntax. I show 2 ways we can work around that. We can use replace on the df, specifying in a dictionary what values in what column (dict inside a dict) syntax, with replace=True. This is horrible, to me! Instead, it makes more sense to treat this as an immutable dataset and simply insert overwrite the series directly: df['column'] = df['column'].replace(...). 
# 
# 
# #datanalytics #datascience #dataengineering #machinelearning #devops
#
# ------
# 🗣 Follow Bryan for more daily #python tips and smash that like button! 💥
#
# 💻 Full repo https://www.github.com/bryangoodrich/python-exercises 👀
# ------
# References: https://pandas.pydata.org/pandas-docs/stable/user_guide/copy_on_write.html

import pandas as pd

pd.options.mode.copy_on_write = True

df = pd.DataFrame({
    "Student": ["Angela", "Berry", "Chris", "Derek", "Elsie"],
    "Grades": [98, 87, 76, 69, 56]
})

# With copy_on_write = False
grades = df.Grades
grades.iloc[0] = 88
df
#   Student  Grades
# 0  Angela      88
# 1   Berry      87
# 2   Chris      76
# 3   Derek      69
# 4   Elsie      56

# With copy_on_write = True
#   Student  Grades
# 0  Angela      98
# 1   Berry      87
# 2   Chris      76
# 3   Derek      69
# 4   Elsie      56

grades  # 88 87 76 69 56

with pd.option_context("mode.copy_on_write", True):
    df = pd.DataFrame({
        "Student": ["Angela", "Berry", "Chris", "Derek", "Elsie"],
        "Grades": [98, 87, 76, 69, 56]
    })
    df.Grades.replace(98, 88, inplace=True)  # Error: No change to df!
    df.replace({"Grades": {98: 88}}, inplace=True)  # Will also replace
    df['Grades'] = df['Grades'].replace(98, 88)  # Will change by replacement!
    df


# 🐍 Daily Pandas 🐼
#
# It can be struggling to understand how to build custom aggregation functions for grouped data. But reading the documentation helped show me some examples that can make it intuitive.
#
# By working with the grouped object itself, we can pull out the name of the group value and the dataframe of its subset directly to see what a group contains.
#
# When we think of it as just this, a labeled dataframe you can literally pull out and look at, you can prototype and build out a function that aggregates this exactly how you want it.
#
# You can also call some useful aggregate functions like grouped.size() to get tallys per group or grouped.describe() to get a quick per-group summary!
# 
# #datanalytics #datascience #dataengineering #machinelearning #devops
#
# ------
# 🗣 Follow Bryan for more daily #python tips and smash that like button! 💥
#
# 💻 Full repo https://www.github.com/bryangoodrich/python-exercises 👀
# ------
# References: https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html

import pandas as pd
from numpy.random import randint

dates = pd.date_range('2024-01-01', '2024-03-31')
values = randint(0, 100, len(dates))
df = pd.DataFrame({'Value': values}, index=dates) 
df["weekday"] = df.index.day_name()

grouped = df.groupby("weekday")
for name, group in grouped:
    print(name)
    print(group)
    # Friday
    #             Value weekday
    # 2024-01-05     80  Friday
    # 2024-01-12     79  Friday
    # ...
    # 2024-03-22     56  Friday
    # 2024-03-29     80  Friday
    #
    # Monday
    #             Value weekday
    # 2024-01-01     40  Monday
    # 2024-01-08     12  Monday
    # ...
    # 2024-03-18     59  Monday
    # 2024-03-25     71  Monday

grouped.describe()
#           Value                                                    
#           count       mean        std   min   25%   50%   75%   max
# weekday                                                            
# Friday     13.0  57.538462  25.976321  20.0  32.0  62.0  80.0  95.0
# Monday     13.0  46.692308  29.349573  10.0  12.0  48.0  71.0  99.0
# Saturday   13.0  33.538462  24.649596   0.0  24.0  31.0  34.0  87.0
# Sunday     13.0  48.538462  14.454615  24.0  38.0  47.0  59.0  77.0
# Thursday   13.0  35.000000  25.897233   1.0  23.0  27.0  46.0  88.0
# Tuesday    13.0  49.384615  36.280248   3.0  13.0  56.0  86.0  96.0
# Wednesday  13.0  33.307692  26.995014   0.0  12.0  37.0  49.0  85.0


# 🐍 Daily Pandas 🐼
#
# Some folks find the filtering syntax of Pandas to be a pain (me included!) and would just like to "write SQL." If Spark can do it, why can't Pandas, huh??
#
# In any case, at least filtering can be made EZ as this example shows! You can also handle parameters in the where clause by putting the at symbol before the variable name in the clause. 
#
# I also think it's cleaner than the standard Pandas syntax when you start doing AND and OR clauses in your filters! 
#
# What do you think?
#
# #datanalytics #datascience #dataengineering #machinelearning #devops
#
# ------
# 🗣 Follow Bryan for more daily #python tips and smash that like button! 💥
#
# 💻 Full repo https://www.github.com/bryangoodrich/python-exercises 👀
# ------

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "CityCode": np.random.randint(50, 100, 1000),
    "Population": np.random.randint(400000, 650000, 1000)
})

code = 97
df[df.CityCode == code]  # 25 rows
#      CityCode  Population
# 0          97      479137
# 70         97      508864
# 143        97      500836
# 268        97      558082
# 386        97      607198
# ...

df.query("CityCode == @code")  # 25 rows
#      CityCode  Population
# 0          97      479137
# 70         97      508864
# 143        97      500836
# 268        97      558082
# 386        97      607198
# ...

df.query("CityCode == @code OR CityCode < 52")  # 68 rows
