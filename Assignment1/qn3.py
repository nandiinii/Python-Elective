num = eval(input("Enter the hexa value"))
print("The octal equivalent is {}".format(oct(num)))
print("The binary equivalent is {}".format(bin(num)))
temp = bin(num)
print("The decimal equivalent is {}".format(int(temp,2)))


