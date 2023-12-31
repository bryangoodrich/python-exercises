📊 Open up new career paths with graph analytics! 🐍

There are libraries like networkx and igraph that will do all of this for you, but I want to get foundational and talk about some algorithms. 

In this example, I use the facebook SNAP dataset from Stanford (snap.stanford.edu). It's a space-delimited edge list like 

0 1
0 2
...
4230 85
4230 123

For efficient searching, we want to create an adjacency list. 

The idea is we'll read the edge list once, and for each node we'll create a dictionary entry for the left-hand side. For each target on the right-hand side, we'll add it to a list on that dictionary entry. Thus, we can easily see all the friend connections for a given anonymous id with a simple key lookup.

Next, we'll perform breadth-first search (BFS). The idea is simple. 

1️⃣ Create a set to keep track of whether we visited a node or not (only search it once)

2️⃣ Create a queue (using a double-sided queue here called a deque) to store who we need to search for in our adjaceny list

3️⃣ We prime our search with a start node to search on until we've exhausted all connections

4️⃣ We then iterate, add the node to visited, dequeue (remove) the only thing in the queue at this point, grab the list of friends from the adjacency list for that node, add those friends to the queue. Repeat until done!

I then wrap this module up as something we can call with a given node id to search on. You'll notice we have a total friend count much larger than those visited, because this dataset does not include all the data. So in this case, we're doing a BFS on all available connections in the data, and sometimes those friends aren't in our adjacency list (not a source node). 

Did this all make sense? Have you used graph modeling in your analytics? What applications do you use this for? Let me know in the comments!

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0072-1.png" />
<img src="../../static/0072-2.png" />
<img src="../../static/0072-3.png" />
