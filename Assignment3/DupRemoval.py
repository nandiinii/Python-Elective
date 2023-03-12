num = int(input("Enter the count:"))
l=[]
for i in range(num):
    temp=input()
    val=int(temp)
    l.append(val)
temp=[]
for i in range(len(l)):
    if l[i] not in temp:
        temp.append(l[i])
print("Before Duplicate items Removal: ",l)
print("After Duplicate items Removal: ",temp)
