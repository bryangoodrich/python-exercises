🐍 Daily Python - Data Visualization 🐍

Heat Maps

I love maps! Though, outside of a tool like QGIS or ArcGIS, it's still pretty rough in my mind to do this extremely well. Nevertheless, I know the tools are there in Python! Today I wanted to explore creating a heat map over some point data. 

Using mostly the geopandas and geoplot tutorials, I take a chicago dataset as the basemap boundaries to give reference, and use a groceries dataset as our points. Actually, multipoints, which you'll notice I overwrite those with their centroids so geoplot stops yelling at me!

From there, I can overlay the heatmap with some transparency. Not my best heat map, but I'll explore this further at another day. Managing the data and errors already took too long to deal with 😖

What mapping data do you see in your business area? Do you map it? Do you want to know how? Let me know in the comments. I think this is a ripe area for people to learn more about.

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0050.png" />

# Output

<img src="map.png" />
