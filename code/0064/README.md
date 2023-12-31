Know your data! Important for data modeling, but I think critical for python developers. 

I'm not referring to understanding what data you have here. Today I want to talk about data types and how to manage data in Python. Recently I talked a bit about object-oriented programming (OOP) and how to define custom objects. Personally, that's not my go-to strategy.

Instead, I often use and reuse basic data types when I can. 

For instance, I typically only use proper class objects if I'm defining a custom data container to handle providing a better user interface with the container (monads). But 90% of the time, I use dicts! 

One advantage is I can serialize my data directly into JSON or other compatible storage type without being too fancy. Another is Python dicts are just very useful with the Python standard library (a topic for another day!).

In this example, following my previous demos about pygame, maybe I need to manage some game state. I show how I can easily put the data (not the behavior) into a dict with nested dicts. 

Alternatively, I show we could create class objects just as well, with a lot of boilerplate (i.e., repetitive) code. Sure, we could use dataclasses or other libraries to simply that!

But in the end, the behavior of how game state is used will come to the functions we define. With proper class objects, we may just pass them into functions or we can embed the functionality in the class methods. 

As a functional programmer, I drive toward just using functions. I show here 2 different ways to define updating my game state by moving the player some (x, y) amount. 

In the first case, we pass the game state object (dict) and we update it within the function. The function itself returns nothing (not FP style). 

In the second case, we simply pass in the coordinate shift and return a new game state. Yes, I didn't include game state in the argument list, which we can. Another approach would be to use a state monad, which is why beyond the scope of this exercise! 

Do you prefer basic data types to an ecosystem of objects? What do you think of this example?

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0064-1.png" />
<img src="../../static/0064-2.png" />
<img src="../../static/0064-3.png" />

