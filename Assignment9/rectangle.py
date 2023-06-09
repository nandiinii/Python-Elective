class Rectangle:
    def __init__(self,height,width):
        self.height=height
        self.width=width

    def area(self):
        print("Area: ",self.width*self.height)

    def perimeter(self):
        print("Perimeter: ",2*(self.height+self.width))

rect=Rectangle(2,3)
rect.perimeter()
rect.area()

