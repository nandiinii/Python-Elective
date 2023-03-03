from math import *
x= int(input("Enter the x value in sine series:"))
n= int(input("Enter the value of n:"))
angle = x*(pi/180)
sine=0
j=0
for i in range(1,n+1,2):
    if j%2 == 0:
        sine = sine + (angle**i/factorial(i))
    else:
        sine = sine - (angle**i/factorial(i))
    j=j+1
print("The sum of sine series is {}".format(round(sine,2)))




