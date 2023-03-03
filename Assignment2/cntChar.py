str=input("Enter the string:")
str = str.casefold()
c1=0
c2=0
c3=0
c4=0
l=len(str)
for i in range(l):
    if str[i].isalpha():
        if str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u':
            c1 += 1
        else:
            c2 += 1
    elif str[i].isdigit():
        c3 += 1
    elif str[i].isspace():
        c4 += 1
print("The number of vowels is {}".format(c1))
print("The number of consonants is {}".format(c2))
print("The number of digits is {}".format(c3))
print("The number of spaces is {}".format(c4))

