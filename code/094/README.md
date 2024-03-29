📖 Have you ever wanted to run a machine learning model on textual data? Welcome to the world of Natural Language Processing! 🐍

In this short example, I walk through the ML process

✅ We prepare our spam dataset into a data frame
✅ We split our data into a training vs validation set
✅ We engineer features to feed into our prediction models
✅ We define and fit our Naive Bayes classifier, in this case
✅ We predict our text data set to compare

At this point, some further data exploration and model iteration would be in order! But you can see how few lines of code it really takes to get this rolling.

Now, what is going on here? I compare a bag-of-words model, where we simply look at the frequency of words in each message as the predictor of whether a message is more likely spam vs ham. 

Contrast that with the TF-IDF version that, if I'm understanding this correctly, fits bi-grams and compares the weighted frequency of not just individual words, but pairs of words, across all the messages. 

Result? 🙋

Surprisingly the bag-of-words (BOW) model has 97% accuracy compared to 94% in the TF-IDF one. 

Is this good? This is where a base model would be useful to compare against, and that might be "let's just assum it's not spam." In that case, since spam only makes up about 12% of the data, we'd be right 88% of the time! So really, the improvement, or lift, of these models is that increase in accuracy. BOW lifts our predictive power by nearly 10 points vs TFIDF only 6 points.

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow Bryan for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0094-1.png" />
<img src="../../static/0094-2.png" />

