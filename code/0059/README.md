Managing your Python code in a package can be challenging.

The design is entirely up to you and you're focused on the code, not how things are organized. 

But remember, the point of a package is that someone else--even your future self--are going to benefit from the ease of use. A package is an API, so think of the UX/UI you're providing them. 

In this example, I demonstrate 2 features of this mock package I made called packit. 

In the first instance, we import the package and its module. Now, the way I defined the init module in packit, we only emit the add function. So packit only has packit.add available. 

However, by also importing the module, I can access module-only content like module.TOPMODFLAG. You can define constants and such in the module for easy configurations elsewhere in your package. 

The second example, I'm taking the subpackage which has an init module that imports content from the 2 modules the subpackage contains. 

With a barnyard theme, I have one module containing my class objects Barn and Farm. The other module contains some constant variables that represent animals. Because of this, I can access content from both modules without needing to know which module to go to for content. Instead, I can just use the subpackage to reference content from both modules in one namespace. 

For full code, see the packit library in my python-exercises codebase!

How do you organize your packages?

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0059.png" />

