🐍 Do you have a plan? 📆

When it comes to your data discovery and understanding phase, there are a few common things that always jump to mind. 

In this example, the first screenshot really recaps the last couple examples for preparing the data as tidy data. 

✅ Rename columns as lowercase snake_case titles
✅ Ensure data types are appropriate and parsed correctly
✅ Compute useful items like total = quantity * price

This next phase we go deeper into data understanding and data prepartion. For instance, the invoice total may be easier to digest or identify anomalies if we put them into categories. If you've got an R background, you'll recognize the familiar cut method. 

We define the cut points for our Series and labels for the bins that are created between these break points. I typically save labeling until I know the breakpoints are what I want and are being mapped correctly, since it'll automatically give you labels. Use them! 

Now we can easily see how many nonpositive total invoices we have!

From there, we might start asking questions, like are customers unique to a country? Turns out 8 customers do have sales across multiple countries 🌎

What about those descriptions? Are they unique to a stock code? They're not. But why? 🤚

If we dig into it, we'll find often there are NULL descriptions when the total invoice is not positive. But that's not always true. Sometimes there are just different descriptions for a given stock code, though similar. Maybe we need some data cleaning to make stock code descriptions unique, if that's a business and reporting requirement.

I then show how we can also investigate checking if a given series is all numeric but stored as string, or if there exists negative in some series that shouldn't be. We can easily apply (map) these helper functions accordingly. 

How do you perform data understanding? What's your data strategy? 

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0086.png" />

