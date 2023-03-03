n = int(input("Enter the number:"))
rev=""
sum=0
while n!=0:
    ld=n%10
    rev=rev+str(ld)
    sum=sum+ld
    n=n//10
print("The reverse is {} and the sum is {}".format(rev,sum))



