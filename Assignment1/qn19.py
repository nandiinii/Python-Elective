from math import *
num = int(input("Enter the number"))
temp =num
sum = 0
while num!=0:
    ld = num%10
    sum = sum + factorial(ld)
    num = num//10
if temp == sum:
    print("Krishnamurthy Number")
else:
    print("Not a Krishnamurthy Number")