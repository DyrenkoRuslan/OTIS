import math

def func(x):
    return ((x + math.sin(x)/(math.log10(math.fabs(x - x**4)))) + (math.log(x)), 4)

num = int(input("x = "))
print(func(num))