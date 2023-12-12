import matplotlib.pyplot as plt
import array
import random

class WeightedQuickUnion:
    def __init__(self, N):
        self._count = N
        self.id = array.array('i', range(N))
        self.size = array.array('i', [1] * N)
    
    def connected(self, p, q):
        """ Is set p connected to set q """
        return self.find(p) == self.find(q)
    
    def count(self):
        """ Accessor method (unnecessary?) """
        return self._count
    
    def find(self, p):
        """ Basically find the top rank parent element """
        while (p != self.id[p]):
            p = self.id[p]
        return p
    
    def get(self, p):
        """ Return the item at p """
        return self.id[p]
    
    def union(self, p, q):
        """ The meat of this structure! """
        p_root = self.find(p)
        q_root = self.find(q)
        if (p_root == q_root):
            return
        
        if (self.size[p_root] < self.size[q_root]):
            self.id[p_root] = q_root
            self.size[q_root] += self.size[p_root]
        else:
            self.id[q_root] = p_root
            self.size[p_root] += self.size[q_root]
        
        self._count += 1


class Percolation:
    def __init__(self, N):
        self.uf = WeightedQuickUnion(N*N+2)
        self.grid = [[False for x in range(N)] for x in range(N)]
        self.vTop = 0
        self.vBottom = N*N+1
        
        if (N == 1):
            return
        
        for k in range(1, N+1):
            self.uf.union(self.xyTo1D(N, k), self.vBottom)
            self.uf.union(self.xyTo1D(1, k), self.vTop)
    
    def open(self, i, j):
        self.grid[i-1][j-1] = True
        if (len(self.grid) == 1):
            self.uf.union(self.xyTo1D(i, j), self.vBottom)
            self.uf.union(self.xyTo1D(i, j), self.vTop)
        
        p = self.xyTo1D(i, j)
        self.unionNeighbor(p, i-1, j)
        self.unionNeighbor(p, i, j-1)
        self.unionNeighbor(p, i, j+1)
        self.unionNeighbor(p, i+1, j)
    
    def isOpen(self, i , j):
        return self.grid[i-1][j-1]
    
    def isFull(self, i, j):
        is_open = self.isOpen(i, j)
        is_connected = self.uf.connected(self.vTop, self.xyTo1D(i,j))
        return is_open and is_connected
    
    def percolates(self):
        return self.uf.connected(self.vTop, self.vBottom)
    
    def valid(self, i):
        N = len(self.grid)
        return (i > 0 and i <= N)
    
    def xyTo1D(self, i, j):
        N = len(self.grid)
        # Error checking with valid
        return (i-1) * N + j
    
    def unionNeighbor(self, p, i, j):
        if (not (self.valid(i) and self.valid(j))):
            return
        
        if (self.isOpen(i, j)):
            self.uf.union(p, self.xyTo1D(i, j))


def visualize_grid(x):
    fig, ax = plt.subplots()
    ax.set_aspect("equal")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_xticks(range(N))
    ax.set_yticks(range(N))
    ax.grid(True)
    
    for i, row in enumerate(x):
        for j, val in enumerate(row):
            if val:
                ax.add_patch(plt.Rectangle((j, i), 1, 1, facecolor="blue"))
                
    plt.savefig("plot.png")


N = 10
p = Percolation(N)
while not p.percolates():
    i = random.randint(1, N)
    j = random.randint(1, N)
    if not p.isOpen(i, j):
        p.open(i, j)

visualize_grid(p.grid)
