num = input("Enter the number")
length = len(num)
fdigit = int(num[0])
ldigit = int(num[length-1])
sum = fdigit+ldigit
print("The sum of first digit and last digit is {}".format(sum))
