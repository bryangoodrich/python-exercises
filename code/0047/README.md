🐍 Daily Python - Special Topic 🐍

Today I'm exploring an old topic from when I was doing "mining of massive datasets" from the old Stanford material on Coursera back in the day. I really should just get that certification already! It's got excellent material!

In any case, due to health reasons I'm not going to revisit it too deeply right now. However, the topic of sharding, MinHashing, and Locality Sensitive Hashing (LSH) is just so useful. 

💡Instead of reinventing the wheel, it looks like we can actually just use sklearn to do the heavy lifting to explore the idea. 

📚The data comes from a git repo aimed at this topic. We pull out a list of sentences, use TDIDF to vectorize the data, and build a nearest neighbors model. 

⚙️There's a LSHForest function in the sklearn library, but I guess not in my version (deprecated?). I use this instead to fit the model and train a search engine. I pass in the query "a person and steak" since I saw steak and person mentioned in one of the sentences. How does it do?

💪Turns out it did pretty well. Removing duplicates, that query matched sentences:

> A person is rinsing a steak with water
> A steak is being rinsed with water by a person
> A man is rinsing a large steak

Let me know if you'd like a more complete treatment of LSH on this data. Could you use a quick and dirty data search engine for your own data? Let me know in the comments below! 

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0047.png" />

