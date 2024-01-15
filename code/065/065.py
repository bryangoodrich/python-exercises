import array

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

q = WeightedQuickUnion(10)
q.id
# array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# Everything disjoint

q.union(0, 2)
# array('i', [0, 1, 0, 3, 4, 5, 6, 7, 8, 9])
# 1 -> 2, everything else disjoint

q.union(8, 9)
# array('i', [0, 1, 0, 3, 4, 5, 6, 7, 8, 8])
# 1 -> 2, 8->9, everything else disjoint

q.union(2, 9)
# array('i', [0, 1, 0, 3, 4, 5, 6, 7, 0, 8])
# 1 -> 2 -> 8, 9-> 8 both connected!