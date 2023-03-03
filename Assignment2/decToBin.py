num = int(input("Enter the number:"))
binVal=""
while num!=0:
    rem = num%2
    num=num//2
    binVal = str(rem)+binVal
print(binVal)