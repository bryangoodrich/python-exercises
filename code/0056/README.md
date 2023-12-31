Every Python developer can benefit from knowing decorators.

They're a little obtuse at first, but once you get it, you get it!

The main idea is you're defining a function that returns a function. Python then uses the "@" syntax to shorthand, essentially, this:

foo = timeit(foo)

In this example, I define the classic timeit decorator that will let you print out the time it took to execute a function call. 

The timeit function we define itself takes in a function and uses functools wraps to ensure this decorator (the nested function) keeps the passed in function's name and documentation. This is important for tooltips and when it errors you won't see some ambiguous reference to the nested function throwing the error. 

After that, we have a certain pattern of decoration. We're going to capture a timer before and after we call the function that we're decorating, and then print out that duration. Last, we return the function execution result value. 

Decorators can be thought of in a couple of ways. Sometimes you want to do something before a function is called, which this enables us to do that, like log the inputs being passed in. Or maybe you want to do something after the function call, like log the result value. Maybe before the function call we need to ensure some state is setup correctly, we can handle that logic, divorced for any function that's being called. 

Thus, decorators let us separate concern between what our functions are doing and some extra stuff we might want done with those function calls. So we decorate our function with that common pattern. Pretty neat, huh?


#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0056.png" />

