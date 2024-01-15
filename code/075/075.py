import numpy as np
import matplotlib.pyplot as plt
from scipy import stats  
from sklearn import datasets

fig = plt.figure(figsize=(6, 6))
ax = fig.subplot_mosaic("""
BBBE
AAAC
AAAC
AAAC
""")

iris = datasets.load_iris()
x = iris.data[:,1]  # Sepal Width
y = iris.data[:,2]  # Petal Length
   
x_min, x_max = x.min(), x.max()
y_min, y_max = y.min(), y.max()

x_kern = stats.gaussian_kde(x)
y_kern = stats.gaussian_kde(y)  

x_positions = np.linspace(x_min, x_max, 100)
y_positions = np.linspace(y_min, y_max, 100)

ax['A'].scatter(x, y)
ax['B'].plot(x_positions, x_kern(x_positions))
ax['C'].plot(y_kern(y_positions), y_positions)

ax['A'].set(xlabel='Sepal Width', ylabel='Petal Length')
ax['B'].set(xticks=[], yticks=[])
ax['C'].set(xticks=[], yticks=[])

fig.delaxes(ax['E'])
fig.tight_layout()
plt.savefig("plot.png")
