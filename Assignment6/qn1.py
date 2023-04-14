num=input("Enter the number:")
temp=int(num)
large=0
while temp!=0:
    val=temp%10
    if large<val:
        large=val
    temp=temp//10
temp1=str(large)
pos=0
if temp1 in num:
    pos=num.index(temp1)
print(f"The largest digit is {temp1} at index {pos}")