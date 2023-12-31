Do you clean your data? Be honest! 🐍

Whether we're talking about data pipelines into databases or your Pandas data munging in Jupyter notebooks, it's all the same. We need to have a good understanding of tidy data and what it entails. 

This includes things like having single-word column names, preferrably with snake_case. Having proper data types assigned to respective columns. This includes categories for categorical variables, integers for properly whole numbers or indicators (which can also be category). 

What are your repeated patterns? Do you standardize them?

Continuing the theme of this week on data profiling and data quality, I show how we can leverage the underscore function from the inflection library to quickly clean up our column names. 

Additionally, I compute relevant calculations, like total invoice cost or create numeric version of a code (sometimes non-numeric versions repreat unique "deprecated" values). I also convert labels into categories that make it easier to tally them.

Tomorrow we'll dig further into this area to tidy our data and build contracts for validation and prepare for preliminary exploratory data analysis (EDA).

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0085.png" />

