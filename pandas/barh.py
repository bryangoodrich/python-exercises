# 🐍 Daily Pandas 🐼
#
# If you have some long-format data, but you want to barchart it horizontally, you can easily transpose your data, maybe after an aggregation, and directly do a barh plot. 
#
# #datanalytics #datascience #dataengineering #machinelearning #devops
#
# ------
# 🗣 If you like this post, follow Bryan for daily #python tips, and hit that like button so the algorithms help others see it, too. 
#
# For full code and data on this and other exercises, see https://www.github.com/bryangoodrich/python-exercises
# ------

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Fruit": [
        "Apples", "Apples", "Apples", 
        "Oranges", "Oranges", "Oranges", 
        "Bananas", "Bananas", "Bananas"],
    "Sales": [4, 3, 3, 2, 8, 5, 8, 9, 3]
}

df = pd.DataFrame(data)
_ = df.groupby("Fruit").sum().transpose().plot.barh()

plt.savefig("barh_plot.png")
