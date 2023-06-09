class Complex:
    def __init__(self,a,b):
        self.a =  a
        self.b = b
    def display(self):
        if self.b > 0:
            print("The complex number is: ",self.a,"+",self.b,"j")
        else:
            print("The complex number is: ",self.a,self.b,"j")
    def __add__(self,other):
        p = self.a + other.a
        q = self.b + other.b
        return Complex(p,q)
cmp1 =  Complex(3,4)
cmp2 = Complex(2,-6)
cmp1.display()
cmp2.display()
cmp3 = cmp1 + cmp2
cmp3.display()