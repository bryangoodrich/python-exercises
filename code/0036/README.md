I can honestly say if you can quickly create publication grade visualizations in Python with ease, you have a marketable talent! I used R for a decade, and could do that in my sleep, but I'm riding the struggle bus here! 

More code in the repo, but I want to focus less on code and more the exploratory data analysis. Now I have a background in analyzing energy, working at a utility. So using the Hourly Energy Consumption dataset from Kaggle (see yesterday's post), here are some system level trends for a given year and a specific utility (heatmaps are American Electric Power and the profiles are Duke Energy). 

The heatmaps reveal 2 things. They both show consumption across each hour (cols) across every day (rows). The first shows where nominally most energy is consumed, which is summer and possibly heating loads during winter. The second heatmap normalizes the data as the percent of the daily consumption in each hour. This tells us the timing of most consumption is later in the day. That's expected as system levels! Households vary much more. 

Now if you were to turn these heatmaps on their side and look at the percentages in 2D line graphs, this is what the load profiles reveal, by overlaying every day's hourly load shape. In R, I would have made this transparent and grey so that the more overlap, the more it's like a thickened pencil stroke, and it would look very clean. Couldn't get that to happen in pyplot! 

In any case, the load shapes clearly demonstrate a couple distinct trends, and this is what I hope to tease out with unsupervised learning tomorrow. 

There are several other graphs and analyses I could talk about in this area. If you have anyone that wants consulting in this domain, send them my way! Or hit me up in the chat. I love talking about this stuff, and it's much more interesting at the household level, I think

What analyses would you try? How do you polish your visuals in Python? Let me know in the comments below!﻿

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0036.png" />

# Outputs

<img src="heatmap.png" />

<img src="heatmap2.png" />

<img src="plot.png" />
