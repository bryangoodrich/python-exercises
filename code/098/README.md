So you want to learn APIs? I got you! 🐍

The api.weather.gov site has an easy to use, and free, API for looking at weather data. I could deep-dive into all the ways you can use this API, like how to find your local weather stations and send that to get your historical weather readings. Instead, we'll use my local Sacramento Airport (KSAC) weather station to look at the latest observations. They're usually hourly around 50 minutes. 

A brief primer on REST APIs. A client sends a request to a server at a specific address (URL/URI). This resource is known as an endpoint and could take extra parameters. There are some common verbs to interact with an endpoint: GET, POST, etc., but we'll focus on GET. It's like "SELECT" for data, in one sense. An endpoint responds to a request and that response could be a non-200 status value, indicating something is wrong. But otherwise, in our case, a 200 means we should have JSON data. The requests library lets us immediately convert this response into a dictionary for processing!

So what's this look like? 🙋

1️⃣ Import the requests library that handles all our web stuff.
2️⃣ Define our endpoint we'll call upon.
3️⃣ We parse the JSON and extract the "properties" key.
4️⃣ I build a list of nested values to process.
5️⃣ For each column, I use a dictionary comprehension to build my data record.
6️⃣ From here, I can convert this to a row in a DataFrame or just print to screen!

That's it! Working with APIs is really easy, and most of the nuance is understanding how to process the response. Let me know if you have any thoughts or questions on this. I'm happy to do more web scraping 😃

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0098.png" />

