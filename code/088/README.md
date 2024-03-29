🗒️ Got shingles? 🐍

A key part of textual analysis and preprocessing includes a technique called shingling. A basic text analytical approach is known as a bag-of-words approach, where we just look at the words and their frequency, independent of order. 

But order matters! 🙌

"This service is no good" vs "No, this service is good" mean two very different things!

How can we capture this ordering? Introduce n-grams. If we broke these sentences into bigrams it would become ["this service", "service is", "is no", "no good"] vs ["no, this", "this service", "service is", "is good"]. 

There is an overlap, but now the sets differ between ["is no", "no good"] on the negative sentiment one vs ["no, this", "is good"] on the positive one. 

Similarly, a tri-gram would break these into 3-word sequences. 

In this example, I read a spam data set that starts each line with "ham" or "spam" and then some body of text message. So my import functions will return tuples of label and message words (tokens).

I use example 100 and show how we can break it into n-grams both using the NLTK library and how we can do it in pure python. 

The pure python way is pretty easy: we use a list comprehension to create n sequences of the original word list, shifted accordingly. Then we zip these together into an n-tuple n-gram. 

Notice, also, I use a generator comprehension, which doesn't process the data until you actually iterate over its values. Additionally, zip does the same thing! So the values aren't actually generated until you request them. Efficient storage usage. Does NLTK do this? Not sure, but wouldn't surprise me!

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0087.png" />

