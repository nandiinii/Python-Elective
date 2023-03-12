num= int(input("Enter the count of numbers"))
l1=list()
prime=list()
composite=list()
print("Enter the elements")
for i in range(num):
    temp=input()
    val=int(temp)
    l1.append(val)
flag=0    
for j in l1:
    flag=0
    for i in range(2,j):
        if j%i==0:
            flag=1
            break
    if flag==1:
        composite.append(j)
    else:
        prime.append(j)
print("List:",l1)
print("Prime:",prime)
print("Composite:",composite)

