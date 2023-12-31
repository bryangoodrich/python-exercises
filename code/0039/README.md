So you think you know Lists? What if you only had functions and basic data types, no dicts, no objects? How would you create an iterable type?

References are in my Gist (https://gist.github.com/bryangoodrich/8275787) from years ago when I did this in R, but it's educational in learning functional programming, and is related to the topics of closures and monads that I've mentioned in previous Saturday posts. 

The idea is simple here. We create a list as a function that encapsulates data (closure) and we can access this by either requesting ("selecting") the head or something else. We use the head and tail functions to retrieve the value or the function that encloses the tail. We can think of it as building a list like a queue that is terminated by the empty_list, our terminal node. Conceptually, it's not unlike a linked list, but using functions to patch it all together. 

Additionally, I introduce a map function for us to apply a function to list elements, just like the built-in map or doing list comprehensions.

What do you think? Did it make sense? Would you like to see the rest of this exercise with other functors for filtering, reducing, and selecting list values more pythonically? Let me know in the comments below!

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0039.png" />

