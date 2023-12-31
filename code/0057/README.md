
Combining decorators is another important use of this feature you should know as a python developer. 

Here I update the previous day's example by adding 2 new decorators for logging (printing) the inputs and function call outputs, so unlike my previous example, function examples foo and bar aren't doing that explicitly. Now the functions focus on what they do.

To understand how this "stacking" of decorators work, it's no different than function composition. 

A single decorator is equivalent to foo = tictoc(foo).

Multiples: foo = log_output(log_inputs(tictoc(foo)))

Lastly, notice I use the lru_cache from functools. This decorator stores the results of a function it decorates (memoization) according to the inputs. We see that instead of actually calling the decorated function when we run bar with the same input, it just returns the value from the cache!

How do you use decorators?

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0057.png" />
<img src="../../static/0057-1.png" />

