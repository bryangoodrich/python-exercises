Should you use duckdb? If you like faster queries and using less storage space, then yes! Here's a quick analysis I did.

First, we create 10M random data points and load these into a sqlite and duckdb instance via file import. We run a row-level lookup by id, an aggregation query, and then measure the clock time. This is far from an optimal testing strategy, but going for quick and dirty here!

Results? DuckDB stored the data in 1/3 the SQLite file size and performed both queries around 25x faster. Yeah, I'm impressed! 

What sort of queries do you think would be a better comparison? Any other databases you'd like to see compared? Let me know in the comments below!

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help other’s see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0026.png" />

<img src="../../static/0026-2.png" />
