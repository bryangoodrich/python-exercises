Analytics in #pyspark is truly easy. If you're a #python developer, or even just know #SQL, you are equipped to write scalable distributed big data #analytics! 

This toy example demonstrates a domain I've worked in for the last decade: energy consumption. Suppose we have some hourly kWh and daily weather data. Further, we want to compare daily usage to the cooling degree days (CDD), defined as the number of average degrees above 65F. While we can do this entirely with SQL queries using the SparkSQL API, I want to demonstrate the logic using the Dataframes API. 

To achieve this data model, we need to aggregate our hourly usage to daily total consumption. Also, we need to compute the CDD and join these data sets together by day. Now everything is clean, so this is straight-forward, but you can see how we can define all the steps in isolation and combine the Spark logic very similarly to how you might reason this in SQL. In the next example, we will explore these data further and fit a statistical model. Stay tuned!

Have you taken a Spark training course that left you unprepared for handling real data? Have you struggled with large scale SQL processing in databases or Pandas? Have you tried Polars?

<img src="../../static/0008.png" />
