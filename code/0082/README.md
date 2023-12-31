🐍 Keep your data in motion 🚀

Have you wanted to go beyond batch jobs or maintaining multiple jobs processing the same data?

Kafka acts as a data broker, where publishers write data into a topic. You can think of it as a named queue, but as consumer, you can think of it like reading an endless file that keeps being appended into. 

We can use PySpark to structure reading this stream, line by line, as if it were a structured table dataframe, giving us the flexibility of writing common SQL like data flows, but without having to manage batch windows.

Moreover, streams feed streams. We can read data from one topic and write the results into another topic. Likewise, multiple jobs can read from the same topic, being at different points in the "file". One could be real-time alerting while another is doing hourly batch windows.

In this example, I simulate an electric utility data set. My producer simulates meter data as JSON records and writes to a "meters" topic. The data looks like this:

{device: '001', interval: 15, endtime: '2023-12-20 08:00:00', kwh: 16.39}

I generate 4 devices, two with 15-minute intervals and the others 60-minute, and each has its own mean and standard deviation for its energy consumption. 

The consumer reads this raw data from the topic, parses out the JSON values, and flattens them as separate columns. Now it's like any old dataframe.

The next challenge is two-fold. 

1️⃣ We'll stream the 15 minute data into a new meters-15 topic.
2️⃣ We'll write the hourly data into meters-60 topic. 

Now the first is straight-forward. We filter the data frame and send it off. The second we can add an hours column to the dataframe and send it off to its topic. But this is the power of streams, we can also aggregate that 15-min dataframe to an hourly summation, and also send it into the meters-60 topic!

This is how we can do complex data processing without requiring large batch jobs or webs of batch jobs. One stream, but we pipe it to topics as needed.

Caveat, this code (in the repo) doesn't fully work. So it's really conceptual at this point. I can use the provided kafka console consumer to validate data flows, but my aggregation isn't working! If anyone is a structured streaming pro, I'd welcome any advice. This is a new area of PySpark to me, and I'm enjoying the journey 😀

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0082.png" />

