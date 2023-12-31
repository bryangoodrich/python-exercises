Every data scientist starts with data exploration, cleaning, and exploration, right? Do you build reusable code and modules to streamline that process? 🤨

Here is one approach to capturing some key information using Pandas. I take the online retail invoices dataset from UCI and saved it as a parquet file. Then in this analysis, I read in the invoices data and immediately map its pandas data types to more descriptive labels. This can feed reporting or similar user-facing dashboards where documentation is easier to consume than code 😂

Then we build ourselves a summary DataFrame that will show us the data types, NULL counts, and percent of the data set these occupy. Compare that with an easy call to describe to see the numeric summary as well. 

Why is this an improvement? 🙌
✅ Pandas tells you the non-NULL counts, requiring you to math out how many are NULL, the actually important information.

✅ We also display the percent NULL, so we can make judgement calls on whether that is acceptable or requires imputation.

✅ As already stated, the type mapping makes it easier and can be customized to our audience. 

What are your go-to summaries and analyses when viewing a new dataset? Do you automate these sort of checks? Stay tuned, I'll be talking about more data quality analysis this week!

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0084.png" />

