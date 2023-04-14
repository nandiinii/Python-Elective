f1=open("txt2.txt","r")
f2=open("sample1.txt","w")
content=f1.readlines()
for line in content:
    if line!='\n':
        f2.write(line)       
f1.close()
f2.close()