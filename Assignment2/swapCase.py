str =input("Enter the string to swap cases:")
l=len(str)
temp=""
for i in range(l):
    if str[i].isalpha():
        if str[i].isupper():
            temp = temp+str[i].lower()
        elif str[i].islower():
            temp = temp+str[i].upper()
    else:
        temp = temp+str[i]
print("The string after swapping cases is")
print(temp)