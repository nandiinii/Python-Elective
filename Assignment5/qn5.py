from math import factorial
def nCr(n,r):
    return factorial(n) // (factorial(r) * factorial(n-r))
print(nCr(5,2))
