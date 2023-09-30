While threads and ThreadPoolExecutors (concurrent.futures) has been around forever now, a new paradigm has emerged in #python that is not uncommon to JS developers. 

In this toy example, we create 2 asynchronous functions to process a data set and to process batches within that data set (the first could contain the logic for partitioning, but it's hardcoded here). We can see it takes very little to setup up an asyncio pipeline!

Do you use asyncio in your work flows and applications? Do you know the differences between asyncio, thread pools, and processor pools and when to choose each? 

<img src="../../static/0004.png">
