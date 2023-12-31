Let's talk about disjoint sets and its applications. 

My last 2 posts went into the Union-Find data structure, plus how we can use it in a model of 2D percolation. Now we're going to run a monte carlo simulation doing the same thing as yesterday, but thousands of times. 

Now I forget exactly why we did this in the Princeton Algorithms class on Coursera. You might think, if I randomly open cells in the 2D grid, it'll take about 50% of the cells to be open for a connection from the top of the grid to connect to the bottom of the grid, allowing flow to percolate from top to bottom. 

This is actually a hypothesis we can test, and the answer for a 10x10 grid is actually we need about 59% of the cells open. 

So in this example, copying what we did in our Java class, I create a stats object that will run the simulations upon initialization, and then we can interact with the object to explore the aggregate model. I could use this object to then do hypothesis testing, p-values, etc. 

I'm not going to do that, and I don't entirely recommend this approach, being the opposite of "pythonic". Nevertheless, it works and I think is a neat conclusion to this exploration. 

To note,

1. When I originally wrote this code in 2015, it took 4 minutes on whatever Python version I was using at the time to do this exact same experiment. Today, it's a fraction of a second! That's insane!! 🤯

2. Another area you'll find UF used in the wild is in network/graph algorithms. Kruskal's minimum spanning trees, for instance, will add weighted edges until a connected component is created, avoiding cycles and some other issues. I've matured in this area in the last decade, and feel even more inclined to study network analysis now that I can understand all this 😂

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0067.png" />

