Do you want to raise your python skills to the next level? You must become experienced with package management. 

Now I'm not going to talk about the packages you install. That can be another day! 

Instead, I'm referring to how you bundle your code together for easier maintenance, sharing with coworkers or the community, and how to reuse modular code so each of your projects aren't reinventing the same wheel. Or worse, doing it differently everywhere.

A package in Python is a folder. Specifically a folder with an __init__.py file. Modules are just files. So we can say a package contains an __init__ module that is called when you import the package. 

A module is just a script file, but it's where you can organize your code into collections of objects, variables, functions, and such.

Additionally, your modules can import other modules, both within the package and from other external packages (called dependencies). I won't get into all of that here. 

In the slides today, you can see the tree structure of my 0058 package. It contains an __init__ module and a topmod module. It also contains a __main__ module I'll get to in a moment. The rest, we'll save for another day.

Now the init module includes a docstring (always document your stuff!) and imports a function from the topmod module that, you can guess, adds two numbers together. 

The main module is special. If you didn't know, you can call modules from the CLI like they're applications. You just have to add the -m flag to specify you're telling python to run a module. However, that's not what we're doing here. We're actually calling the package! Python sees that you're requesting a folder, not a module file, and so it looks for that __main__ module and calls it. 

So you can see how everything ties together and I can run my package like a module, and it logs to screen how everything else is being called. When you import a package, you're just running whatever is in the init module. This gets called whether you're importing the package or a module within it or some object in the module. 

Are you packaging your code??

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0058-1.png" />
<img src="../../static/0058-2.png" />
<img src="../../static/0058-3.png" />
<img src="../../static/0058-4.png" />

