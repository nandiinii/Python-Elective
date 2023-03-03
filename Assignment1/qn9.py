from math import *
num = int(input("Enter the number "))
temp = factorial(num)
sum=0
while temp != 0:
    ld = temp%10
    sum =sum + ld
    temp=temp/10
print("The sum of digits of factorial of the number is %d"%(sum))