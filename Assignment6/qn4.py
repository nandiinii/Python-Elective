num=int(input("Enter the number to check if it is power of 2:"))
if num&(num-1)==0:
    print("Power of 2")
else:
    print("Not a Power of 2")
