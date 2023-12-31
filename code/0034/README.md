Want to make some functions faster? You need to know caching!

This snippet trims out a bit of detail, but the main thrust is that we have a lot of caching options available. For instance, Redis and Memcache are very common caching servers you can run, and I provide an init.sh in today's code folder for you if you need to install on an apt-based Linux system (Codespace). Of course, we can cache in the app's local memory as well, as I use with a dictionary and using the functools lru_cache decorator. 

The key here is your function needs to be pure. What this means is that it doesn't have side effects. But what does that mean?? Simply, for any given set of inputs you will get the same output. This allows us to store the arguments as keys with the function result as its values. Thus, while it may take awhile to perform an action the first time, every subsequent call simply gets the result from cache. 

This is even more powerful in recursive cases, as exemplified by factorial or fibonacci implementations. Since each recursive call is held in memory, the repeated references to previously computed values become instant lookups. 

I show the output for the DictCache and lru_cache, but still need to work on the Redis and memcache examples because they don't handle argument tuples like the other caches do. I also extended the dict to have a .set method to be consistent with the .get and .set methods of the redis and memcache objects. Maybe next week!

New to decorators? Let me know, I love functional programming! Do you use cachcing in your data pipelines? Tell me about your use-cases in the comments 😀

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0034.png" />

