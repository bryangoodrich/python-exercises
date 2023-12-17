import array
import random
import sys
import time
import numpy as np

rlst = [random.randint(0, 100) for _ in range(10**7)]  
rray = array.array('i', rlst)
print("Object size comparison")
print(f"Size: {sys.getsizeof(rlst):>15,} bytes | "
      f"{rray.buffer_info()[1] * rray.itemsize:>15,} bytes")

print("Native summation")
start = time.time()
sum(rlst)   
end = time.time()
list_time = (end - start)
start = time.time()
sum(rray)
end = time.time()
array_time = (end - start)  
print(f"Time: {list_time:>15.3f} sec | {array_time:>15.3f} sec")

print("Numpy summation")
start = time.time()
np.sum(rlst)   
end = time.time()
list_time = (end - start)
start = time.time()
np.sum(rray)
end = time.time()
array_time = (end - start)  
print(f"Time: {list_time:>15.3f} sec | {array_time:>15.3f} sec")

# Object size comparison
# Size:    89,095,160 bytes |    40,000,000 bytes
# Native summation
# Time:           0.060 sec |           0.127 sec
# Numpy summation
# Time:           0.407 sec |           0.003 sec