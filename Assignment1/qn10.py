from math import *
num = input("Enter the number")
length = len(num)
fdigit = int(num[0])
ldigit = int(num[length-1])
num1 = sqrt(fdigit)
num2 = sqrt(ldigit)
print("The square root value of first digit: {}".format(num1))
print("The square root value of last digit: {}".format(num2))
