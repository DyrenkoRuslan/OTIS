import math

def func(x):
    if x >= 3.7:
        return x + math.sqrt(x) + math.sqrt(4*x + 7)**1/3
    if -1.5 < x < 3.7:
        return math.tau(x) + x**2
    else:
        return math.log(math.fabs(x), math.e)
   

for i in range(10):   
    print(i, func(i))