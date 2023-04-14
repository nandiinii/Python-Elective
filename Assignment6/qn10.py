f1=open("sample.txt","r")
f2=open("enc.txt","w")
l=f1.readlines()
key= int(input("Enter the key value between 0 and 25:"))
for line in l:
    line = line.casefold()
    str1=""
    for i in range(len(line)):
        if(line[i]==" "):
            str1 = str1+" "
        else:
            x=ord(line[i])-97
            y=(x+key)%26
            val=y+97
            str1 = str1+chr(val)
    f2.writelines(str1)
f1.close()
f2.close()