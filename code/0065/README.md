Data structures can be hard for Python devs not from a CS background. 

The reason, I think, is it's all theoretical. There is little application in most cases for analysts or data scientists, unless they know how to use these structures. I want to talk about a structure that differs from many in basic DS classes (lists, trees, etc.), and has a direct scientific application. 

I learned the Union-Find (Disjoint sets) structure in the Princeton Algorithms class you can take on Coursera (Best. CS. Class. Ever. Period.), using Java. This is a rough migration of that code to Python.

The union-find or disjoint sets structure provides an efficient way to take a list of items and link them together into sets. The 2 operations you benefit from here are

1. Can I find if an item is in a set?
2. Can I union disjoint sets together into one set. 

The application was to a percolation model--like water through coffee grinds or electricity through copper. Later I'll show how this can be used to solve statistical problems in this area.

Let me know if the implementation doesn't make sense, but to me, we can think of sets like conceptually linked lists and sets are connected if they share the same root node. 

We can see this by example. The id is an array object I initialize as size 10, all items (numbers) are disjoint. I union 0 and 2 together and we see that the item in position 2 is replaced by reference to 0. I then union 8 and 9 so we see the last 2 elements are both reference to 8 now. Then I union 2 and 9. 

Now your intuition might be we'd replace the last 2 elements as 0s, but that's not the case. We only change reference of the root node so now position 8 refers to 0 and 9 still refers to 8 which refers to 0. Thus we have 2 sets that are connected via item 8. 

Tomorrow I'll demonstrate how this solves our percolation problem!

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0065-1.png" />
<img src="../../static/0065-2.png" />

