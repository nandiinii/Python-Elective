import math
def fact(n):
    if n==0:
        return 1
    else:
        return n * fact(n-1)
def cos(x,n):
    sum=0
    for i in range(n):
        sum += ((-1)**i) * (x**(2*i)) / fact(2*i)
    return sum
x=float(input("Enter the x value in radians: "))
n = int(input("Enter the number of terms: "))
print("Sum of cosine series = ",cos(x,n))