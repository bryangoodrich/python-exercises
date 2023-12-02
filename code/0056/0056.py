from time import perf_counter, sleep
from functools import wraps
from random import uniform

def timeit(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        duration = perf_counter() - start
        print(f"Function {fn.__name__} took {duration:.2f} seconds.")
        return result
    
    return wrapper

@timeit
def foo(x):
    print(f"Running foo with {x}")
    sleep(uniform(0.1, 0.5))
    return x + 5  

@timeit
def bar(x):
    print(f"Running bar with {x}") 
    sleep(uniform(0.7, 1.2))
    return x * 2

if __name__ == "__main__":
    print(foo(5)) 
    # Running foo with 5
    # Function foo took 0.25 seconds.
    # 10
    print(bar(6))
    # Running bar with 6
    # Function bar took 0.78 seconds.
    # 12