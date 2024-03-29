Let's finish this 100 days of code with some generators! 🐍

The idea of generators I've talked about multiple times and pretty sure I've done a day on them already. Unlike standard functions that return a value, this terminates the call to a function. A generator instead yields a result which indicates that the flow of the program will return, but we can iterate on the function by starting back where it was last yielded. Typically this is within some loop.

So generators are useful for data management. Instead of iterating over something and fully materializing it in memory, the iterator of a generator, like we see in functions like range, zip, map, enumerate, and so on are providing a promise to get the next value, if it exists. This way if we zip 2 massive lists together, we're not doubling the size in memory. Instead, the iteration will just go fetch the next 2 items from each list and pair them together. Useful!

I'm working on a day ahead forecasting model using LSTM (long short-term memory) and one of the ways you have to prepare your recurrent neural network data is to provide your dataframe chunked up into segments of training and validation sets. But if we do this for every record in our dataframe we're duplicating the data quite a lot! 

So instead, I use a generator to do the slicing and at any time the iteration is using a single subset of our dataframe, not producing N-Buffer duplicates of the dataframe of size N. 

Let me know if you have generator questions. I want to do more work with asyncio, which leverages this generator idea to the extreme so Python can handle async processes. It's worth knowing!

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/100.png" />

