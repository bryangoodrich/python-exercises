🐍 Are you keeping up with Python changes? 🐍

With the last few versions, you can see a strong trend of Python moving to become more functional in its design. 

What is functional programming? One way to describe it is FP emphasizes declarative syntax over imperative syntax. 

If you're familiar with SQL, the difference here is that FP is like describing the shape of your output versus programming how to get it done. Let's look at an example.

1️⃣ We define a tree structure with a leaf node class and inner node class, where the leaf stores values and inner nodes represent the binary tree structure with left and right node references. We also define a function that we'll dig into more in a second.

2️⃣ We then define our tree instance by building up from some leaf values until we're at a root tree. I show this in ASCII so it makes sense!

3️⃣ Lastly, we see how this summation can be performed to recursively walk the tree to the leaves and sum up each leaf value. We can do this from the root or any inner node at a given layer (sub-tree). 

Now the meat of this being functional shows up in a number of ways. 

First, we define a data type using the OR construct as a Node is either a LeafNode OR an InnerNode. These are called algebraic data types in FP speak.

Second, notice how using the match operation we dispatch not through a series of ifs in an if-else block. Instead, we describe a pattern that we're looking for using this new match expression (not a statement). 

Another way of thinking about a match expression is that expressions evaluate to a value. So we're not using control flow to dispatch via if-else statements. By describing the structure of what we want, the match expression will evaluate accordingly, and because the 2nd match condition is a recursive one, it'll eventually evaluate to a summation we're after as it walks down the tree. 

What do you think? Does it make you look at recursion differently? Have you started using match expressions in your programs?

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit github.com/bryangoodrich/python-exercises
------

<img src="../../static/0071-1.png" />
<img src="../../static/0071-2.png" />
<img src="../../static/0071-3.png" />
