# github.com/bryangoodrich/python-exercises
# code/0026/0026.py

import random
import sqlite3
from subprocess import run as cmd
import time

import duckdb

NUM_ROWS = 10000000
data = [(random.randint(1, NUM_ROWS), round(random.uniform(0, 1), 6)) for _ in range(NUM_ROWS)]
with open("data.csv", "w", encoding="ascii") as fh:
    for item in data:
        _ = fh.write(f"{item[0]},{item[1]}\n")

sqlite = sqlite3.connect('sqlite.db', isolation_level=None)
duck = duckdb.connect('duck.db')

sqlite_cursor = sqlite.cursor()
duck_cursor = duck.cursor()
sqlite_cursor.execute('CREATE TABLE data (id INTEGER, value REAL)')
duck_cursor.execute('CREATE TABLE data (id INTEGER, value FLOAT)')
cmd('sqlite3 sqlite.db ".mode csv" ".import data.csv data" ".quit"', shell=True, check=True)
duck_cursor.execute("COPY data FROM 'data.csv' (DELIMITER ',')")

### Part II
# code/0026/0026.py

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start_time:.4f} seconds")
        return result
    return wrapper

@timeit
def run_test(conn, query, *args):
    cursor = conn.cursor()
    if args:
        cursor.execute(query, args)
    else:
        cursor.execute(query)
    return cursor.fetchall() if args else cursor.fetchone()

lookup_id = random.randint(1, NUM_ROWS)
ID_LOOKUP_QUERY = 'SELECT * FROM data WHERE id = ?'
AGGREGATION_QUERY = 'SELECT AVG(value) FROM data'

run_test(sqlite, ID_LOOKUP_QUERY, lookup_id)
run_test(duck, ID_LOOKUP_QUERY, lookup_id)
# run_test took 0.4359 seconds  (SQLITE)
# [(2481363, 0.859215), (2481363, 0.747233), (2481363, 0.907479)]
# run_test took 0.0167 seconds  (DUCKDB)
# [(2481363, 0.859215), (2481363, 0.747233), (2481363, 0.907479)]

run_test(sqlite, AGGREGATION_QUERY)
run_test(duck, AGGREGATION_QUERY)
# run_test took 0.5161 seconds  (SQLITE)
# (0.49998983869924984,)
# run_test took 0.0211 seconds  (DUCKDB)
# (0.4999898386921374,)

sqlite.close()
duck.close()
