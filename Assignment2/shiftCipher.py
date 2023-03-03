str=input("Enter the string to use Caesar Cipher:")
str = str.casefold()
str1=""
key= int(input("Enter the key value between 0 and 25:"))
for i in range(len(str)):
    if(str[i]==" "):
        str1 = str1+" "
    else:
        x=ord(str[i])-97
        y=(x+key)%26
        val=y+97
        str1 = str1+chr(val)
print(str1)

