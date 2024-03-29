I've seen a lot of people lately talking about method chaining, both on LinkedIn and YouTube. Do you know what it is? 🐍

The basic idea is simple enough. If you understand classes, instead of a method returning a value, you have it return the object itself. Thus, you mutate the object and because the returning object is the same thing, you can chain another call to its methods. 

We see this in strings, like "some,csv,set,of,data\n".strip().split(",")

We see it in Pandas and PySpark DataFrames.

Some time ago I talked about using functional programming approach where you can pipe together functions on a dataset so the output of one function is the input to another, like in the Bash terminal on Linux you can chain commands with |. I created a class object that lets you chain together Python function calls so instead of "h(g(f(x)))" we can do "x | f | g | h" or "x >> f >> g >> h" by overloading the __or__ or __rshift__ method on a Pipe class.

In that spirit, I provide an example of this pipelining using method chaining!

As you can see, it's pretty easy to wrap our data into a pipeline object that lets us chain (pipe) one function call into the next. This isn't the most interesting example of method chaining, compared to the initial ones above, but it does show an overlap in the concept of function composition or piping between OOP and functional programming.

Do you use method chaining?

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0092.png" />

