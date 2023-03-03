from math import *
n=int(input("Enter the number to find its sqrt:"))
approx=0.5*n
better=0.5*(approx+n/approx)
while better!=approx:
    approx=better
    better=0.5*(approx+n/approx)
print(round(approx,5))