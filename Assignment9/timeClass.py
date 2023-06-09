class Time:
    def __init__(self,hr=0,min=0,sec=0):
        self.hr = hr
        self.min = min
        self.sec = sec
    def __str__(self):
        return '%.2d:%.2d:%.2d'%(self.hr,self.min,self.sec)
    def __add__(self,other):
        
        h1 = self.hr +other.hr
        m1 =  self.min + other.min
        s1 = self.sec + other.sec
        return Time(h1,m1,s1)
t1 = Time(2,34,21) 
t2 = Time(13,4,20)
t3 = t1+t2
print(t1)
print(t2)
print(t3)
   