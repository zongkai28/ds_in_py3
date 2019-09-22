# python 3.7.3
import time

start_time = time.time_ns()

for a in range(0, 1001):
    for b in range(0, 1001):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print("a, b:%d, %d."%(a, b))

end_time = time.time_ns()

print("eclipsed time:%d ms."%((end_time - start_time)/1000000))