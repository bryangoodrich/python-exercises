Have you ever wanted to link your applications or data pipeline jobs together in some way? Then think about information-as-a-service. How do we build a service oriented architecture? 🐍

Yesterday I showed how queues can help us communicate messages between functions. This example we leverage RabbitMQ to facilitate this message bus between separate isolated applications. 

The producer.py application will take 10 random samples from a mock data set and publish that message as a small JSON string. It will sleep for half a second between messages.

The consumer.py application once activated will connect to RMQ and wait for data. You can terminate the consumer at any time with CTRL+C. Otherwise, each time you run the producer, the messages will eventually be picked up by the consumer, with 1 second between reads. 

While I show the output of each app, in reality you can spin up 2 separate terminals, after starting your RabbitMQ server, and run them simultaneously. The producer can keep being run to generate more messages, and the consumer will keep spitting our the messages, showing their coordination while being completely decoupled! Bam!!

Why is this important? 🙋‍♂️

Scalability - We can have multiple instances of these applications writing and reading from the queue independently

Modularity - Each application can be designed in isolation. They just need to agree on the message structure. 

I could go on, but where might we use this? ✈️

Consider a logging application. Yes, there are plenty on the market, but conceptually let's work it out. 

Suppose we have 100 differen't data pipelines that run at 1 AM and if each has to write to the same database table, this requires session connections, table locks, etc. Instead, think of each job as a producer writing their log metadata or metrics to a queue. 

The consumer can be 1 application (or scaled up as needed) that reads off the queue, sets up the database connection, and inserts the logs or metrics sequentially. These apps can even live on the same server, but we're managing resources because the consumer doesn't even have to run all the time. Maybe it kicks off during idle times when the job server isn't busy. Lots of options!

How do you use message bus architecture and queues? Caveat, I've never actually had the chance to use RabbitMQ, so I'd be happy to be told the "right" way to make production code with pika or some other library! This is a new domain for me 😀

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0080.png" />

