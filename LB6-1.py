import math
a=float(input("first"))
b=float(input("second"))
h=float(input("step"))
x=a
y=0.0
for i in range (10):
    y=x*math.sin(x)+math.e**x
    y=round(y,4)
    print(i,"   ",x,"   ",y)
    x=x+h
    x=round(x,1)
    if x>b:
        break

