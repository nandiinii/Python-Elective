f1=open("txt1.txt","r")
f2=open("sample2.txt","w")
content=f1.read()
f2.write(content)
f1.close()
f2.close()
print("File is Copied")