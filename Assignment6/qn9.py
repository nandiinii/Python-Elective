def fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n - 1) + fib(n - 2))
n=int(input('Enter n: '))
print('nth fibonacci term: ',fib(n-1))
print("Fibonacci series")
for i in range(n):
    print(fib(i))