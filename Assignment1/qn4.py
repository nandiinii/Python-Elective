from math import *
print("Point on a circle")
x1=int(input("x1= "))
y1=int(input("y1= "))
print("Centre Of circle")
xc=int(input("xc= "))
yc=int(input("yc= "))
p=(y1-yc)**2
print(p)
q=(x1-xc)**2
print(q)
radius = round(sqrt(p+q),2)
print("Radius is {}".format(radius))
area = pi * radius * radius
print("Area is {:.2f}".format(area))
