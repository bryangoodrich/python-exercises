Let's talk about categorical variables in statistical modeling. This is a common occurance in data when we want to look at whether a data generating process is statistically changed by the existing or exclusion of a given category. Now I won't go into details here, feel free to ask, but this is an area with a lot of nuance. 

Instead, this is a simple example to show how to get started. Given a data set like the following, taken from Kaggle (https://www.kaggle.com/datasets/gauravduttakiit/real-estate-price) and stored in the codebase, we have the following features

price: 234314.144, 228581.528, 281626.336, 401255.608, 458674.256
size: 643.09, 656.22, 487.29, 1504.75, 275.46
year: 2015, 2009, 2018, 2015, 2009
view: No sea view, No sea view, Sea view, No sea view, Sea view

So we normalize the price to be a bit easier to read (divide by 1000) and perform what pd.get_dummies would do by adding an indicator column (0/1) based on the view feature. From there, we fit the model accordingly and use Seaborn to plot it. I'll have you know, Chat-GPT sucks at describing how to use Seaborn for any use case! 😂

What does this show? The categorical coefficient indicates a $56,000 increase to price when there is a sea view vs not, on average. It's a level shift in the lienar fitted line. 

What else could we have done? Modeled the interaction term between the view and size or year, because maybe the effect is mediated by house size in some way or differs by year. But interaction models will be a future exercise!

Let me know what you think in the comments below.

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0045.png" />

# Output

<img src="plot.png" />
