☀️ If you want to dazzle people with your data viz, you need to try real-time analytics! 🐍

You might think sure, Power BI and other BI tools do this, but we're Python developers! We got this 💪

In this example, following this week's daily examples, we set up a simple Kafka producer that simulates a stock price by randomly picking some deviation from the previous price. A Markov process! 📈

I then used a Jupyter notebook and captured the output in a consumer to print the values, ensuring I am getting what I expect. It's just JSON of timestamp and price. 

Then we do the real fun, we setup a consumer to plot this data in real-time! 🚀

At least for me, I spent a solid 5x on getting the visualization to work than all the other stuff I did this week. Lots of documentation reading, too! Turns out, once you understand the stuff you need to make Jupyter refresh properly, it all works out. See the repo for the full details.

What real-time reporting use-cases do you want to tackle or have tackled? I'd love to hear your stories!

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------
