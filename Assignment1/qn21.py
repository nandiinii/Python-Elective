num = int(input("Enter the number:"))
arr=(0,1,2,3,4,5,6,7,8,9)
flag =[0,0,0,0,0,0,0,0,0,0]
while num!=0:
    ld = num%10
    if(flag[ld]==0):
        temp = bin(ld)
        print("The binary value of {} is {} ".format(ld,temp))
        flag[ld]=1
    num = num//10
