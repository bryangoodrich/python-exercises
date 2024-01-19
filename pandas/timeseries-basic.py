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
