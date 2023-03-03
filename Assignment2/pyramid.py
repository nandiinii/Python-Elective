n = int(input("Enter the n value for the height of the pyramid:"))
s=""
for i in range(1,n+1):
    for j in range(0,i):
        s = s + str(j+1) + " "
    print(s)
    s=""
    print()