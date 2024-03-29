😡 How is your argument game? 🐍

I'm not talking about argumentation. I mean your function arguments. The other day I talked about *args, and I want to flesh this out a little deeper. Some of the examples here are taken from the Real Python page, very nice: https://realpython.com/lessons/positional-only-arguments/

1️⃣ Decorators are a great example

They show off a number of things, and you don't need to know all about decorators to get this example. 

The main idea is they add some extra behavior to your function by "wrapping" it in some extra stuff. We do this by creating a function that defines a function and returns that inner function. 

Thus, when we decorate the function, it's like renaming the function after passing it through this decorator function. In this case, tictoc will time the function call and print out the seconds it took. But we also need to call the function and handle any arguments it takes. The pattern is (*args, **kwargs). Like before, *args is a tuple of all positional arguments and **kwargs is a dictionary of named arguments. We capture them and pass them along to whatever function is being decorated. 

Therefore, we don't need to know anything about the function being decorated. We simply handle passing along the arguments. Win! 💪

2️⃣ Positional-Only Arguments

If you look at the float function definition you'll see it's float(x=0, /). This used to be mere documentation, but now that "/" is part of our syntax. It enables us to define positional only arguments. If you call float(x=5) you get a syntax error! 

I use this to define a norm function that handles a 2D or 3D vector. It makes no sense to specify x, y, or z. Instead, just pass them in positionally, which I do with tuple unpacking. 

By contrast, we can use a "*" to indicate keyword arguments afterwards. I show this with the greetings function. If you want to change the greeting, you have to use a keyword argument!

3️⃣ Put it all together now! (positional / either * keyword)

In the last example, we can use these patterns to differentiate positional only vs some that can be named or not, and those that are keyword-only. This gives you full control of the API you're building with your code as described by PEP 570 (if you want to be a Python stud, read PEPs! 😂): https://peps.python.org/pep-0570/

How do you argument?? 

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow Bryan for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0097-1.png" />
<img src="../../static/0097-2.png" />
<img src="../../static/0097-3.png" />

