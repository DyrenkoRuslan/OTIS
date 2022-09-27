import math
a=float(input("a = "))
b=float(input("b = "))
h=float(input("h = "))
x=a
y=0.0
while (x<=b):
    y=x*math.sin(x)+math.e**x
    y=round(y,4)
    print(x,"   ",y)
    x=x+h
    x=round(x,2)