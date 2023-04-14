def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter the n value for cos series:"))
x=float(input("Enter the x value between -1 and 1:"))
series=1
temp=0
for i in range(2,n+1,2):
    if temp%2==0:
        series -= (x**i)/fact(i)
    else:
        series += (x**i)/fact(i)
    temp+=1
print(f"The value of cos series is {series}")