num = int(input("Enter the 3-digit number to check if it is an armstrong number:"))
temp=num
s=0
while num!=0:
    ld = num%10
    s = s + ld**3
    num = num//10
if s == temp:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")