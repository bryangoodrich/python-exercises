Exploratory Data Analysis (EDA). It's a cornerstone of any good analysis as its your first chance to understand the data. For this example, I'm looking at CC purchases data at https://www.kaggle.com/datasets/arjunbhasin2013/ccdata

I saw somebody analyzing this data, and after a few dozen pages of graphics, I realized the value of a plot I used to do in R. This is my attempt, thanks to Chappy, for replicating it in Python! Full code is on my GitHub.

If you look at a correlation table, it's symmetric across the upper and lower triangles and the diagonal is all ones. So why not do a heat map of the correlation values in one triangle, do a scatter plot with linear fit that represents that correlation value visually, and then do the univariate histogram or Kernel Density Estimation (KDE) plot on the diagonal. That's the idea, and I think it came out alright.

While not as pretty or as easy to do as in R, it's a start! What do you think? What else could we do on this NxN facet plot? What would you like to see next? Let me know in the comments!

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0042.png" />

# Output

<img src="corr.png" />
