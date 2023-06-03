n=int(input("Enter the number to check if it is an armstrong number:"))
temp=n
sum=0
l=len(str(n))
while n!=0:
    ld=n%10
    sum += ld**l
    n=n//10
if(temp==sum):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")