phoneNo = int(input("Enter the mobile number(10 digits)"))
num = phoneNo%100
print("The binary value is {}".format(bin(num)))
print("The octal value is {}".format(oct(num)))
print("The hexadecimal value is {}".format(hex(num)))
