If you run into memory issues, generators can help!

What is a generator? It's a data structure you can iterate over, like lists and tuples, but it uses much less memory because the values are only presented when requested. 

You can think of generators as a promise to have values in the future or a way to evaluate the results later than when it was defined. 

I show 2 examples here.

First, we can walk through the Fibonacci sequence without having to compute the whole thing. Instead, we simply compute the next value on request. 

The key here is a generator function yields a result. This pauses execution of the function until the "next" function is called on it, which is how iteration occurs. At that point, execution resumes after the yield, which in this case we compute the next Fibonacci sequence value.

Second, we can use generator comprehesion by simply using parentheses. For all purposes, this behaves like a list, but we don't actually store all the intermdiate values. 

If you're using very large lists to do something, or processing each value takes a lot of time, you can have more control by working with only one value at a time but still have all the iterable benefits. 

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0055.png" />

