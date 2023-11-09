import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random


def jitter(x, jit=0.35):
    return x + random.uniform(-jit, jit)


N = 500  # Number of students
schools = ["School A", "School B", "School C"]
df = pd.DataFrame({
    'school': [random.choice(schools) for _ in range(N)],
    'scores': np.random.normal(70, 10, N),
    'shade': [random.randint(0,250) for _ in range(N)],
})

school_ids = dict(zip(schools, [1,2,3]))
df['id'] = df['school'].apply(lambda school: school_ids[school])
df['pos'] = df['id'].apply(jitter)

plt.figure(figsize=(8, 6))
plt.scatter(df.pos, df.scores, c=df.shade, cmap="Blues")
plt.xticks([1,2,3])
plt.gca().set_xticklabels(schools)
plt.xticks(rotation=45) 
plt.grid(True)
plt.savefig("plot-jittered.png")

plt.figure(figsize=(8, 6))
plt.scatter(df.id, df.scores, c=df.shade, cmap="Blues")
plt.xticks([1,2,3])
plt.gca().set_xticklabels(schools)
plt.xticks(rotation=45) 
plt.grid(True)
plt.savefig("plot.png")