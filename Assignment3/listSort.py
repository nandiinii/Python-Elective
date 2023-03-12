num = int(input("Enter the count:"))
l=[]
for i in range(num):
    temp=input()
    val=int(temp)
    l.append(val)
l2=l.copy()
l3=l.copy()
l2.sort()
l3.sort(reverse=True)
if l==l2:
    print("List is sorted in ascending order")
elif l==l3:
    print("List is sorted in descending order")
else:
    print("The list is not sorted")
