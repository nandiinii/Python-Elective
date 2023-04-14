f1=open("num.txt","r")
f2=open("prime.txt","w")
f3=open("composite.txt","w")
lst=f1.readlines()
for i in lst:
    num=int(i)
    flag=0
    for j in range(2,(num//2)+1):
        if num%j==0:
            f3.writelines(i)
            flag=1
            break
    if flag==0:
        f2.writelines(i)
f1.close()
f2.close()
f3.close()