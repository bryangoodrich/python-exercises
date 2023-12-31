🐍 Daily Python - Statistics 🐍

Holt-Winters Exponential Smoothing

When I would use R for forecasting, I liked the simplicity of Holt-Winters smoothing. At least it was simple to apply, I never really thought much about what the model or parameters meant! 

Luckily, it's very easy to implement using the statsmodels library. HW is great for fitting short to medium-term forecasts for certain models. In this case, I'm reusing the hourly energy consumption for Duke Energy back on day 35. Seasonally, a good predictor of tomorrow's usage is yesterday's usage, and this shouldn't change in the short term. 

With these assumptions, I ignore trend and select an additive seasonality of 24 hours to then forecast the next 24. As we can see in the plot, it's not a bad fit. 

What models do you try in your forecasts? Let me know in the chat! 

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0052.png" />

