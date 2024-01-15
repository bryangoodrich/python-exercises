class Pipe:
    def __init__(self, value):
        self.value = value
    
    def map(self, fn):
        return Pipe(fn(self.value))
    
    __rshift__ = map
    __or__ = map
    
    def __getattr__(self, method):
        return Pipe(getattr(self.value, method)())
    
    def __repr__(self):
        return repr(self.value)


def add5(x):
    return x+5


result = Pipe(5) >> (lambda x: x**2) >> add5
print(result)  # Output: 30

result = (Pipe("Jerry Berry") 
    | (lambda s: s.split(" "))
    | (lambda x: ",".join([s.lower() for s in x]))
)

print(result)  # Output: "jerry,berry"
