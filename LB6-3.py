import math
a=float(input("a = "))
b=float(input("b = "))
h=float(input("h = "))
x=a
y=0.0
spisok_x=[]
spisok_y=[]
spisok=[spisok_x,spisok_y]
while (x<=b):
    y=x*math.sin(x)+math.e**x
    y=round(y,4)
    spisok_x.append(x)
    spisok_y.append(y)
    print(x,"   ",y)
    x=x+h
    x=round(x,2)
print(spisok)