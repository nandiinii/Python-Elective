class Point:
    def __init__(self,a=0,b=0):
        self.a = a
        self.b = b
    def __str__(self):
       return f'({self.a},{self.b})'
    def __lt__(self,other):
        self.a < other.a
        self.b < other.b
    def __add__(self,other):
        p = self.a + other.a
        q = self.b + other.b
        return Point(p,q)
    def __sub__(self,other):
        p = self.a - other.a
        q = self.b - other.b
        return Point(p,q)
pt1 = Point(2,4)
pt2 = Point(-2,5)
print(pt1)
print(pt2)
pt3 = pt1 + pt2
print(pt3)
pt4 = pt1 - pt2
print(pt4)
if(pt1 < pt2):
    print("Point 1 is smaller")
else:
    print("Point 2 is smaller")