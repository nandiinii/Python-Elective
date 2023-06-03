str=input("Enter the string to use Caesar Cipher encryption:")
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
str1=input("enter the string to decrypt it: ")
str2=""
for i in range(len(str)):
    if(str1[i]==" "):
        str2 = str2+" "
    else:
        x=ord(str1[i])-97
        y=(x-key)%26
        val=y+97
        str2 = str2+chr(val)
print(str2)
