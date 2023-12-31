Do you know how to make your data structure work for you?

Yesterday I talked about the union-find (disjoint sets) data structure. It provides the ability to efficiently identify if 2 sets are connected (you know, not disjoint).

An example is a 2D percolation that could represent water through a coffee filter or electricity through a wire. We could do 3D but that'd be complicated!

I first show how we use this percolation model of a 10x10 grid. The goal is to randomly open cells in this grid until the model percolates. 

To represent this, I actually link 2 "virtual" rows at the top and bottom. If the virtual top and bottom connect, because we can easily check this with our Union-Find, we say water flows from top to bottom!

I plot the final grid at the end, where cells that are open are blue. In my Algorithms class, we would color this differently were the cells connected so you can easily see the path that percolation is taking. But that'll be another day!

Lastly, I show a stripped down copy of the Percolation class that uses the Union-Find structure, converting between the 2D model and our 1D data structure. 

Do you use data structures in this way to model real-world stuff? What else might you use this data structure for?

Tomorrow I'll show how we can do some statistics with the percolation model to do some mathematical modeling. Stick around for the fun!

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0066-1.png" />
<img src="../../static/0066-2.png" />

# Output

<img src="plot.png" />
