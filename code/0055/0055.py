def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for value in fibonacci_generator(10):
    print(value)  # 0 1 1 2 3 5 8 13 21 34 ...

query_template = "SELECT * FROM table WHERE dt='{}'"
dates = ('2023-01-01', '2023-01-02', '2023-01-02')
queries = (query_template.format(dt) for dt in dates)
for query in queries:
    print(query)

# SELECT * FROM table WHERE dt='2023-01-01'
# SELECT * FROM table WHERE dt='2023-01-02'
# SELECT * FROM table WHERE dt='2023-01-02'