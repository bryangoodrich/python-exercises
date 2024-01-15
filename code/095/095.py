import math
from random import randint

def distance(x, y):
    return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)

def compute_distance(*points):
    size = len(points)
    if size in (0, 1):
        return 0
    pairs = zip(points[:-1], points[1:])
    distances = (distance(a, b) for a, b in pairs)
    return sum(distances)

data = [(randint(1,10), randint(1,10)) for _ in range(10)]
compute_distance([])                        #      0
compute_distance(*data[0:1])                #      0
compute_distance(data[0])                   #      0
compute_distance(data[0], data[1])          #  3.606
compute_distance(*data[0:2])                #  3.606
distance(data[0], data[1])                  #  3.606
compute_distance(data[0], data[1], data[2]) #  8.608
compute_distance(*data[0:3])                #  8.608
compute_distance(*data)                     # 46.225
