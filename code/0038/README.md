Let's cap this week's analysis with some Python forecasting! 

Using the same Kaggle Hourly Energy Consumption data, and some lightweight munging, we pop this into an ARIMA and Prophet model. Thanks to Chappy (Chat-GPT), I learned about that last one. It's a Meta developed library that is pretty slick. 

We clearly see from the PACF graph that there is a weekly and 24 hour cyclical pattern. I'm not going to act like I know what I'm talking about, but I did add a seasonal component for this and hey, the day-ahead forecast wasn't terrible!

Compare that to fitting a prophet model that returns a lot of extra information, including automatically determining seasonal and trend components, and we get a nice plot that aligns with the ARIMA model--I wasn't totally off 😂 

I had plans to do a LSTM deep learning model for this, but maybe next week? If there's interest, I'll definitely commit time to that. Let me know in the comments! This was a fun set of exercises this week. 

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0038.png" />

# Output

<img src="acf.png" />
<img src="arima.png" />
<img src="prophet.png" />
