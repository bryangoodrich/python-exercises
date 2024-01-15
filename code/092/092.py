class Pipeline:
    def __init__(self, data):
        self.data = data
    
    def map(self, fn):
        self.data = fn(self.data)
        return self

def add5(x):
    return x + 5

def double(x):
    return 2 * x

def negate(x):
    return -x

Pipeline(5).map(add5).map(double).map(negate).data  # -20

Pipeline(100) \
    .map(add5) \
    .map(negate) \
    .map(double) \
    .map(double) \
    .data  # -420
