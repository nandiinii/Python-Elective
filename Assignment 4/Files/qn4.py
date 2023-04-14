from math import *
f1=open("txt4.txt","r")
lst=f1.readlines()
numlist=list(set(lst))
numlist.sort()
f2=open("sample3.txt","w")
f2.writelines(numlist)
f1.close()
f2.close()
