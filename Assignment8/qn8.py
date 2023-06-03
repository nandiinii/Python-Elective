num = int(input("Enter the count:"))
l=[]
for i in range(num):
    temp=int(input())
    l.append(temp)
list_positive = []
list_negative = []
for i in l:
    if i < 0:
        list_negative.append(i)
    else:
        list_positive.append(i)
print(f"List of positive numbers: {list_positive}")
print(f"List of negative numbers: {list_negative}")