n=int(input("enter the count:"))
print("Enter the values")
num=[]
for i in range(n):
    val=int(input())
    num.append(val)
numcount={}
for i in num:
    numcount[i]=numcount.get(i,0)+1
maxcount=max(numcount.values())
print("Mode:")
for i in numcount:
    if numcount[i]==maxcount:
        print(i)