import time
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def bigo(x, func):
    N = len(x)
    name = func.__name__
    const, xs, ys = np.zeros(N), np.zeros(N), np.zeros(N)
    for i, item in enumerate(x):
        start = time.time()
        func(item)
        xs[i] = len(item)
        ys[i] = time.time() - start
    
    X = np.vstack([const, np.log2(xs)]).T
    model = LinearRegression()
    model.fit(X, np.log2(ys))
    plt.scatter(xs, ys, label=name)
    plt.xlabel('Input Size')
    plt.ylabel('Runtime (s)')
    plt.xscale("log")
    plt.yscale("log")
    plt.legend()
    plt.title('Runtime Scaling (log-scaled)')
    plt.savefig("scatter.png")
    return model

def bad_sum(x):
    total = 0
    for item in x:
        total += item + sum(x)
    return total

x = np.logspace(10, 20, num=11, base=2, dtype=int)
data = []
for n in x:
    data.append(list(np.random.rand(n)))

fit = bigo(data, sum)
print(fit.coef_[1])
fit = bigo(data, sorted)
print(fit.coef_[1])
fit = bigo(data[:-1], bad_sum)
print(fit.coef_[1])
