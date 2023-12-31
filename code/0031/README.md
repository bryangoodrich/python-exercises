Who doesn't love the Central Limit Theorem? What .. Nobody? Okay, I think it's a nice introduction to bootstrapping (resampling) methods.

The CLT basically means you can stop worry about your data being normal, especially in linear modeling. You're fitting an expectation (average), and as this demo shows, you can have a non-normal data distribution that has very normal statistics. 

We resample the non-normal data, even of only N=30, and we will get a normal distribution of its sample means. Increase that N and you'll get an even smoother shape. The joy of resampling!

Additionally, I show how easy you can use bootstrapping to fit empirical confidence intervals. So even if you don't have a well-defined model, as long as you can resample your dataset, you can capture the variation embedded in it to generate your confidence bounds. This is especially useful in small N situations.

Do you use boostrapping/resampling methods in your statistics? What else would you like to know? Leave a comment in the chat! 


#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0031.png" />

# Output

<img src="plot.png" />
