num = int(input("Enter the count:"))
l=[]
for i in range(num):
    temp=input()
    val=int(temp)
    l.append(val)
cnt=0
num=0
temp=[]
for i in range(len(l)):
    ctr=l.count(l[i])
    if(cnt<ctr):
        cnt = ctr
        num = l[i] 
print("The number with maximum count {} is {}".format(cnt,num)) 

        
