import math
def fact(n):
    if n==0:
        return 1
    else:
        return n * fact(n-1)
def series(x,num):
    sum=0
    for i in range(num):    
        sum += x**i/fact(i)
    print(f"The sum of series is: {sum}")
n = int(input("Enter the number of terms: "))
x = int(input("Enter the value of x: "))
series(x,n)