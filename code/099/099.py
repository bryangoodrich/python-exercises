from dataclasses import dataclass
from functools import lru_cache

@lru_cache(maxsize=None) 
def fib(n: int) -> int:
    match n:
        case 0:
            return 0
        case 1:
            return 1
        case _: 
            return fib(n-1) + fib(n-2)


@dataclass
class Point:
    x: int
    y: int

def locate(point: Point) -> str:
    match point:
        case Point(0, 0):
            return "Origin"

        case Point(0, _):
            return "On the y-axis"

        case Point(_, 0): 
            return "On the x-axis"

        case Point(x, y) if x > 0 and y > 0:
            return "In quadrant I"

        case Point(x, y) if x < 0 and y > 0:
            return "In quadrant II"

        case Point(x, y) if x < 0 and y < 0:
            return "In quadrant III"

        case Point(x, y) if x > 0 and y < 0:
            return "In quadrant IV"

if __name__ == "__main__":
    import sys
    n = int(sys.argv[1])
    print(fib(n))  # 100 -> 354_224_848_179_261_915_075
    
    print(locate(Point(5, 3)))   # "In quadrant I"
    print(locate(Point(0, 5)))   # On the y-axis
    print(locate(Point(-3, 2)))  # In quadrant II
