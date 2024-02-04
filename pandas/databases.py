# 🐍 Daily Pandas 🐼
#
# Hands down, the DuckDB integration with Python/Pandas is amazing. Now, I think it could be even better (why doesn't that pd.merge work?!)
#
# This shows how easy we can register our dataframe in the database, push the merge (join) to pure SQL, and return your result efficiently back as a DataFrame.
#
# If, like me, you prefer SQL to Pandas syntax, this can be a dream and easier access for certain people to help maintain data pipelines by just knowing SQL and much less Python.
#
# #datanalytics #datascience #dataengineering #machinelearning #devops
#
# ------
# 🗣 Follow Bryan for more daily #python tips and smash that like button! 💥
#
# 💻 Full repo https://www.github.com/bryangoodrich/python-exercises 👀
# ------

import pandas as pd
from duckdb import connect

students = pd.DataFrame({
    'id': [1, 2, 3],
    'teacher': [1, 1, 2],
    'name': ['John', 'Jane', 'Joe'],
    'grades': [89, 93, 76]
})

conn = connect()
conn.execute('CREATE TABLE teacher (id INTEGER, name VARCHAR)')  
conn.execute("INSERT INTO teacher VALUES (1, 'Mary'), (2, 'Peter')")
conn.register('student', students)

# This does not work! IT SHOULD!!
# df = pd.merge(students, conn.table('teacher'), left_on='teacher', right_on='id')

df = conn.execute('''
SELECT 
    S.id as student_id,
    S.name as student_name,
    S.grades as grade,
    T.name as teacher
FROM 
    student S 
    JOIN teacher T
    ON S.teacher = T.id
''').fetchdf()
#    student_id student_name  grade teacher
# 0           2         Jane     93    Mary
# 1           3          Joe     76   Peter
# 2           2         Jane     93    Mary
# 3           3          Joe     76   Peter
# 4           1         John     89    Mary
# 5           1         John     89    Mary


