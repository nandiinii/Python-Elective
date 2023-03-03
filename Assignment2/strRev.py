str = input("Enter the string to check if it is palindrome or not:")
str = str.casefold()
temp = str[::-1]
if temp == str:
    print("Palindrome")
else:
    print("Not a Palindrome")