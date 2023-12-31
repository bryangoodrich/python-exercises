🐍 Daily Python - Data Analytics 🐍

Grouping Sets

Reading through Zach Wilson's interviewing blogs at https://blog.dataengineer.io, one stuck out to me. In it, he talked about grouping sets. 

While I've known about these and other SQL operators like ROLLUP and CUBE, I've never actually had a use for them. That's usually something we leave to Power BI or the reporting layer to resolve off the data warehouse. Of course, if we can model accordingly between PBI and our database to leverage these, maybe less DAX and more preprocessing can be done at the database layer! That's a point for another day, however. 

I can also see how this would be very advantageous in a big data space where you won't have the benefits of a database system, and due to scale you cannot push that onto the reporting tool or have users wait for these to be computed each time on the backend. Treat them like batched updated OLAP cubes. 

Instead, I wanted to see how we can simulate this in Python. First, what are grouping sets? You basically define what groups you want to group on, so you do multiple at once. Let's take the classic Titanic dataset. I want to look at the average fare per passenger class (1, 2, 3) and sex (male, female). I want to see them for each of those groupings separately, and for none of them (i.e., the overall mean). We would write this in SQL as

SELECT Pclass, Sex, Mean(Fare) as Fare
FROM Titanic
GROUP BY GROUPING SETS
(), (Pclass, Sex), (Pclass), (Sex)

In other words, a grouping set is simply specifying a combination of groups to append together in the final result set. The expectation is that when you group by one category but not another, it's as if you were to select something like "Pclass, NULL as Sex, Mean(Fare)", in the case of grouping (Pclass). Make sense?

So the best I can find is that we have to effectively do this the hard way and do all the grouping separately! That is what I do, get rid of the existing dataframe indexes, then concat these groups together for the final result. I added the grouping sets to the end of each line for clarity.

Pclass     Sex        Fare
   1.0  female  106.125798  (Pclass, Sex)
   1.0    male   67.226127  (Pclass, Sex)
   2.0  female   21.970121  (Pclass, Sex)
   2.0    male   19.741782  (Pclass, Sex)
   3.0  female   16.118810  (Pclass, Sex)
   3.0    male   12.695466  (Pclass, Sex)
   1.0     NaN   84.154687  (Pclass)
   2.0     NaN   20.662183  (Pclass)
   3.0     NaN   13.707707  (Pclass)
   NaN  female   44.479818  (Sex)
   NaN    male   25.633935  (Sex)
   NaN     NaN   32.305420  ()

Do you have a use case for this? Is there another approach you would suggest? How about if we try ROLLUP (hierarchies) or CUBE (all permutations)? Let me know in the comments below!

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0049.png" />

