print("The prime numbers within 100:")
for j in range(2,101):
    if j > 1:
       for i in range(2, j):
           if (j % i) == 0:
               break
       else:
           print(j)
