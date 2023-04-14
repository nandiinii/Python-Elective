f1=open("txt3.txt","r")
str=f1.read()
str=str.replace("\n"," ")
words=str.split(" ")
words.sort()
for w in words:
    if len(w)!= 0:
        print(w,len(w))
f1.close()

