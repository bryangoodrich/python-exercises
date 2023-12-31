If you've never created your own custom Python objects, you're missing out!

The basic goal of objects is to customize the information you're collecting inside the object. The class object is a blueprint for what your custom data type will contain and be able to do. 

I am just scratching the surface in this example where a User contains a name, email, and list of posts they've made. The post itself is an object that contains some content, a date posted, and a reference to a user that made the post. In this way, our posts and users are coupled. 

Additionally, by defining the special double underscore (dunder) functions, we're overwriting default object behavior or providing it where it is missing. There is a lot here, but I'm just showing how we can customize its display via overloading the str method. 

Note, functions inside a class are called methods or object methods, because they define the behavior of what an object can do. 

I also demonstrate a basic walkthrough of how we can instantiate (create object instances) our objects and use them. 

Do you use objects in your code?

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0060-1.png" />
<img src="../../static/0060-2.png" />

