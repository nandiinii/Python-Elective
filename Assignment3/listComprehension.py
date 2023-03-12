from math import *
l1=[2,3,4,24,56,60,90,120,12,9]
l2=[x for x in l1 if (log10(x)/log10(3))%1==0]
print(l2)
l3=[x for x in l1 if x<100 and x%3==0]
print(l3)