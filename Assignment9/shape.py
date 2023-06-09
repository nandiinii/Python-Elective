from abc import ABC
from math import *
class Shape(ABC):
    def area():
        pass
    def circumference():
        pass
class Rectangle(Shape):
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def area(self):
        print("Area: ",self.l * self.b)
    def circumference(self):
        print("Circumference: ",2 * (self.l + self.b))
class Circle(Shape):
    def __init__(self,r):
        self.r = r
    def area(self):
        print("Area: ",pi * (self.r**2))
    def circumference(self):
        print("Circumference: ",2 * pi * self.r)
rect = Rectangle(2,3)
rect.area()
rect.circumference()
circ = Circle(3)
circ.area()
circ.circumference()