from math import *
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        self.area1 = pi*(self.radius**2)
        print("The area is: ",self.area1)
    def __gt__(self,other):
        return self.area1 > other.area1

c1 = Circle(3)
c2 = Circle(2.5)
c1.area()
c2.area()
if(c1 > c2):
    print("Circle 1 has greater area")
else:
    print("Circle 2 has greater area")    