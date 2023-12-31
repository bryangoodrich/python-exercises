Want to build reliable, scalable apps? 🙋‍♂️ 

You need to understand message bus architectures and queues! 🐍

Suppose you have an application that produces some information. Our consuming app(s) want to use this information in real-time. However, consumers may use this data at different times and at different rates. This decoupling is the heart of a message bus.

➡️ Use a queue to store the data for a given consumer.
➡️ Producers populate this queue with data.
➡️ Clients pop off data from the queue on their own schedule.

That's it! 

I simulate this using Python queues and multithreading. The producer uses some random mock data and writes at a rate of 0.1 to 0.5 seconds while the consumer thread reads this data off the queue, in order, at a rate of 0.4 to 0.8 seconds. The consumer terminates once the queue is empty.

Where might we see this applied? 

Consider you have a producer application taking in photos from users or scraping them from the internet, and we have a consuming application that will do image classification. 

➡️ The consumer will be more CPU intensive and take longer than the faster IO bound producer. 

➡️ The producer saves images to an S3 bucket and writes the location URI to a queue. 

➡️ The consumer or consumers can pull off these paths from the queue and start processing the images independent of the producer and can be scaled at different rates than the producer, such as 1 producer and 10 classifiers running simultaneously. 

➡️ Each classifier can then become a producer and write the URI to another queue indicating completeness and classification 

➡️ Then another consumer picks up this information and logs it into a database table. 

We can start to see how decoupled, independent applications can be linked together via message bus architectures or service-oriented architectures (SOA). It gives flexibility, easier unit testing and area of concern, and enables easier scaling of each component independently. Not to mention, these components can become reusable and participate in multiple buses, just by changing what queues they interact with. That's just a configuration change!

Do you use queues or build SOA apps? I'd like to hear your use cases

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0079-1.png" />
<img src="../../static/0079-2.png" />
<img src="../../static/0079-3.png" />

