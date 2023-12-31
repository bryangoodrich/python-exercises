Your modeling efforts must begin with data munging (do we still use that word?), whether statistical or machine learning modeling. Today I'm going to start a multi-part walkthrough preparing and building an unsupervised learning (clustering) model from stuff I presented in earlier days. 

Specifically, today we look at the Hourly Energy Consumption Kaggle dataset. 

It comes in several time series files with schema <Datetime, SiteName_MW>. We want to build a feature set we can model like <Site, Date, Hour1, ..., Hour24> with the hourly MW values in the columns. So how do we get there?

First, we combine the separate time series files. Then we add some new columns (date, hours), aggregate (avg) duplicate readings because of daylight savings, and pivot from long-to-wide format. Lastly, we save this in a nice compressed parquet format, converting the 12 MB archive from Kaggle into a 4 MB feature set ready for modeling. 

Tomorrow, we'll do some data exploration with visualizations. 

These are all common tasks when working as an analyst, data engineer, or data scientist, so I hope this is useful. How might you have gone about this? What other transformations might you have done? Let me know in the comments below! 

Data source: https://www.kaggle.com/datasets/robikscube/hourly-energy-consumption

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0035.png" />

