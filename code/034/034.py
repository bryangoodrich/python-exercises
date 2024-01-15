import memcache
import redis
import sys
from time import time, sleep
from functools import wraps, lru_cache

class DictCache(dict):
   def set(self, key, value):
      self[key] = value

def timeit(fn):
    @wraps(fn)
    def _timeit(*args, **kwargs):
        start = int(round(time() * 1000))
        try:
            return fn(*args, **kwargs)
        finally:
            end_ = int(round(time() * 1000)) - start
            print(f"Total execution time: {end_ if end_ > 0 else 0} ms")
    return _timeit

def cached(cache):
    def decorator(fn):
        @wraps(fn)
        def inner(*args, **kwargs):
            key = args + tuple(kwargs.items()) 
            if key not in cache:
                cache.set(key, fn(*args, **kwargs))
            return cache.get(key)
        return inner
    return decorator

caches = {
    "dc": DictCache(),
    "rc": redis.Redis(host='localhost', port=6379, db=0),
    "mc": memcache.Client(['127.0.0.1:11211']) 
}


if __name__ == "__main__":
    opt = sys.argv[1] if len(sys.argv) > 1 else "dc"
    cache_option = caches.get(opt, "dc")

    @timeit
    @cached(cache_option) 
    def slowprod(a, b):
        sleep(1)
        return a * b
    
    @timeit
    @lru_cache
    def lruprod(a, b):
        sleep(1)
        return a * b
    
    print(slowprod(2,3))  # 1001 ms
    print(slowprod(2,3))  # 0 ms
    print(slowprod(4,5))  # 1001 ms
    print(slowprod(4,5))  # 0 ms
    print(slowprod(5,4))  # 1001 ms
    print(lruprod(2,3))   # 1001 ms
    print(lruprod(2,3))   # 0 ms
