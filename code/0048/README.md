🐍 Daily Python - Data Engineering 🐍

Lambda Architecture

Thanks to Zach Wilson for inspiration. He's opened up his interview prep stuff at https://blog.dataengineer.io and I highly recommend it!

One thing he talks about was Lambda and Kappa architectures, which I know what they are, but have never had the opportunity to work on them in the wild. So why not toy around today?

The main (simplistic) idea of Lambda architecture is you split your data flow into 3 pieces: batch, streaming, and serving layers. I mock this up in 3 files. The batch job leverages day 35 (hourly energy consumption time series) to load a directory of source files into a parquet batch file. 

The streaming job mocks an API pull (weather data) by simply loading the CSV into a Redis cache for serving. If I can get Kafka working nicely in my codespace, I'll use that approach on the Kappa architecture. 

The serving layer, which I haven't really completed (so don't expect full functionality) was to just make those 2 data sets available by a Fast API endpoint where you can filter by utility (site). Ideally, the weather data would merge with the consumption data to feed downstream analytics or machine learning. 

So what do you think? Is this adequately Lambda? What might I try different to better represent it? Let me know in the comments below!


#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0048-1.png" />
<img src="../../static/0048-2.png" />
<img src="../../static/0048-3.png" />

