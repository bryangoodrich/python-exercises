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
