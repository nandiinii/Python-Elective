num=int(input("enter the number to find the sum of digits:"))
sum=num%9
if sum==0:
    sum=9
print(f"The sum of digits is {sum}")