As a python developer, do you understand the difference between a statement and expression? 

Control flow is typically managed through statements. The 2 most common are if-else statements and for-loop statements. You evaluate some condition of the conditional or the loop and then proceed to execute a batch of other statements, controlling the flow of your program.

But do you always need control flow? 

This is far from new, as ternary operators have been around since C days. But the ethos of it, to me, stems from functional programming. We say functional languages are "more expressive" precisely refers to the fact you use expressions over statements. 

The if-else expression shown here demonstrates that if you're using an if-else statement to control the flow of your program just to assign a variable conditionally, you're better off handling that condition in an expression that is just part of that assignment. 

Where might this be ineffective? If instead of a single assignment I'm doing 500! It might be a little crazy to have 500 assignment expressions all evaluating the same condition when you can do it once and then do the group assignment. But whether that makes sense is really dependent on the situation and the developer's tastes. 

Do you keep an eye for where an expression can replace a statement?

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0063.png" />

