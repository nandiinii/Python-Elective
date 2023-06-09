from math import *
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        self.area1 = pi*(self.radius**2)
        print("The area is: ",self.area1)
class Circle1(Circle):
    def __init__(self, radius):
        super().__init__(radius)
    def circum(self):
        self.circ = 2 * pi * self.radius
        print("Circumference: ",self.circ)
circle = Circle1(2.5)
circle.circum()
circle.area()