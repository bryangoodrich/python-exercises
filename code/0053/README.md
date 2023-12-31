🐍 Daily Python - Machine Learning 🐍

Support Vector Regression

I rarely used SVMs back in my R days, and I never actually learned the details of SVR. So today I decided to try this out. I'll dig into the methodology later. 

We use a standard approach to ML training, by splitting our data in an 80/20 format between training and test sets. We define an SVR model from Sklearn, using an RGB kernel. I'll do a post on the kernel trick in the future! 

After that, we train our model and run it against the test set. I also compute the mean of the training set as the predictor for the test set y's as a way to define a baseline model. This is similar to comparing the ANOVA of a model Y~X against the baseline model Y~1, which is just using the expectation of Y as the predictor. We can see our SVR model gives us a nearly 50% reduction in MSE!

Lastly, we plot the fitted terms and the residuals. Not a bad fit and the residuals are adequately random (could use actual statistical tests for these). 

Have you used SVRs before? What applications? I'd love to learn more about this. Let me know in the comments below!

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0053.png" />

# Output

<img src="svn_prediction.png" />

<img src="svn_residuals.png" />
