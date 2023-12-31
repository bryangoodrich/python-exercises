Let's talk about Big-O (time complexity). This is a basic example of how you can use statistics--yeah, there's a reason it's required in CS--to help estimate how long an operation will take to run given some experiments. 

In this instance, I test 3 list operations: sum (linear), sorted (loglinear), and my bad_sum (quadratic), while doubling the input size for each iteration. Then I plot these results. By taking the input size and runtimes, log2 transformed, we can fit a linear model to assist a visual graph analysis, you'll find most people talk about online. 

With these transformed data, the model slope coefficient b represents the O(aN^b) in big-O notation. As we see from these results. Respectively, they're 1 (linear), 1.2 (loglinear), and 2 (quadratic). 

There are good materials on these asymptotic methods in the Analysis of Algorithms taught by Princeton (resources online). Let me know in the comments if you want to talk about the caveats when using these methods!

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0032.png" />

# Output

<img src="scatter.png" />
