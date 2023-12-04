from time import perf_counter, sleep
from functools import wraps, lru_cache
from random import uniform

def tictoc(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        duration = perf_counter() - start
        print(f"Function {fn.__name__} took {duration:.2f} seconds.")
        return result
    
    return wrapper

def log_inputs(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"Function {fn.__name__} called with arguments:")
        if args:
            print(f"  Args: {args}")
        if kwargs:
            print(f"  Kwargs: {kwargs}")
        return fn(*args, **kwargs)
    return wrapper

def log_output(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        print(f"Function {fn.__name__} returned {result}")
        return result
    return wrapper

@lru_cache
@log_inputs
@log_output
@tictoc
def foo(x):
    sleep(uniform(0.1, 0.5))
    return x + 5  

@lru_cache
@log_inputs
@log_output
@tictoc
def bar(x):
    sleep(uniform(0.7, 1.2))
    return x * 2

if __name__ == "__main__":
    print(foo(5)) 
    # Function foo called with arguments:
    # Args: (5,)
    # Function foo took 0.35 seconds.
    # Function foo returned 10
    # 10
    print(bar(6))
    # Function bar called with arguments:
    #   Args: (6,)
    # Function bar took 0.92 seconds.
    # Function bar returned 12
    # 12
    print("Calling bar(6) again (memorized)")
    print(bar(6))
    # Calling bar(6) again (memorized)
    # 12