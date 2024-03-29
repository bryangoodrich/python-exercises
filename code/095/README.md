🐍 While a basic programming concept, it can be deceptively difficult if you haven't been exposed to it. I'm referring here to args and kwargs. If, like me, you come from an R background, this was the "..." other arguments object you can handle to pass along within your code.

Python makes this exceptionally easy because args is just a tuple of positional arguments passed in, but we don't know how many arguments are coming in. 

The most basic example is the adder. You can define a function that takes in x and y and return x + y, but what if you want to add 3 or 4 or ... N numbers together? You don't want to define add3 and add4 and ... addN different functions. You also don't want to require yourself to define it as taking in a list of numbers. You want flexibility!

This is where the args object comes in. In my example, I have coordinates as tuples, randomly created data. I have a distance function to compute the Euclidean distance between any 2 coordinates. 

But look at the compute_distance function. It takes in a *points object. WTF is that? 🙋

Iterables like a tuple can be unpacked, and this syntax is saying we are unpacking positional arguments (or collecting, in this case) some number of arguments into a tuple called points. Because of that, I can cleverly iterate over pairs of points and compute their pairwise distances and then return that total summation. 

In the example use-cases, I show that in the case of 0 or 1 point, we just return a 0 distance. Otherwise, we can pass in the points directly (x, y) or unpack our tuple into them (*(x,y)). We can pass in 2 points or 3 or the entire dataset. 

Python is flexible 🧘

How do you use args? 

What about kwargs? Check back tomorrow! I'll use it with closures (functional programming).

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0095.png" />

