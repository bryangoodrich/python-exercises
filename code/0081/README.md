Ever wondered how to share information between multiple applications simultaneously? It's a lot easier than you might think! 🐍

Kafka is an excellent tool for this purpose. While I'm not going to go through the trouble I spent getting it installed on my codespace (ugh!!), once it's up and running, we can use the kafka_python library to interface with it.

You run the chat app and it asks for your username. Afterwards, it waits for you to send it messages. These go into a Kafka topic that any other chat apps will also subscribe for new messages. Technically, your app gets your message, too, but if your username matches the sender, it won't display it (using a GUID internally would be smarter, obviously) 

The class I create here handles all client information and interaction with the Kafka service, using multithreading to both receive messages from the topic as well as publishing chat messages for the user into the topic. 

I put 3 console tabs side-by-side and chatted with myself using this app. I was surprised how easy this was to setup. Might have been better if I right-aligned received messages to better resemble chat apps. 

Why is this important 🙋‍♂️

I could go on for pages about the use of pub-sub model and the million use-cases of Kafka. The short of it ... it's an awesome way to stream real-time data from multiple sources (producers/publishers) to multiple targets (consumers/subscribers). 

Next time, I'll show how we can do real-time data processing and analytics using Kafka and Spark. Stay tuned!

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------ 

<img src="../../static/0081.png" />

