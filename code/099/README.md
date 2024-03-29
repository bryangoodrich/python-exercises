I want to drill in the joy of functional programming before this 100 day series is over! 🐍

I show 2 examples of using FP features in Python. First, we use the new match statement to demonstrate how slick your recursive statements can become. 

While the typical example would just check "if n in (0, 1) return n" and then return fib(n-1) + fib(n-2), you can see how those 2 paths have a different structure. It makes sense, and may even be less typing, but by dispatching your paths through the match expression solves them under 1 pattern. 

Additionally, what I like, is the use of expressions over statements. This is a key facet of functional programming. An expression evaluates to a value. So this match version, in one sense, just evaluates to the answer, whereas the standard form uses a conditional statement to handle the base case and then based on that we end up evaluating one of 2 return statements.

Like I said .. slick! 🛢️ 

The functools also provides you the lru_cache will will save the output of any call to the function based on its input (think of a dictionary with keys as the inputs and values as the function return values). Without this, even computing 100 would take forever! But with lru_cache it finishes instantly! 💪

In the 2nd example I define a point class (holds and x,y position) and shows the real use of the match expression. While the first example is like any old case statement, but the point of match isn't to just match values to responses. It's to look for patterns on the thing being matched. 

As you can see, we can match on values of an object's shape, like if both x and y are 0, one of them is 0, or they're both nonzero and their values fall within some range. While this example is pretty straight-forward, and not very useful, it's intuitive and shows how powerful match can be! 

Do you match? Let me know in the comments below!

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0099-1.png" />
<img src="../../static/0099-2.png" />

