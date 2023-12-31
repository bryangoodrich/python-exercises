How can we use unsupervised learning (clustering) to help identify energy usage patterns in hourly energy consumption data?

Using yesterday's visualizations as a guide, we can see distinct consumption patterns in system level load shapes for Duke Energy. Now, I do this at the household/business level, and it's a bit more useful (more variation!), so to keep this simple I'm not expecting meaningful insights to pop out of this today. I just want to show the methods.

Using the same parquet file, we clean up the data and pull a random sample (could do the whole thing, it's still not that big) to get 1000 random days of consumption normalized as the percent used in any hour of that day. These will latch onto the timing of consumption events, which for summer tend to be in the afternoon, and if electric heating is present, we see that in the morning/evening during winter time.

We fit both KMeans and DBSCAN models to this feature set, aiming for 5 clusters (1 for each season and an outlier/flat group). I then use the centroids of KMeans and the data group means to represent the entire cluster. I could also plot the actual data lines like yesterday and color code according to each cluster, but this is easier to see for now.

Let me know what you think! There is a lot of nuance in this analysis we could dig into, like how to best fit model parameters, how much data to use, should I sample across multiple utilities so each is like a separate household?

Let me know in the comments below!

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0037.png" />

# Output

<img src="kmeans.png" />

<img src="dbscan.png" />
