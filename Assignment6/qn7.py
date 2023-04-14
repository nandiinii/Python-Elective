val=float(input("Enter the binary number:"))
temp=str(val)
l=len(temp)
li=temp.split(".")
ip=int(li[0])
dp=li[1]
dec=0.0
while ip!=0:
    for i in range(0,l):
        num=ip%10
        if num==1:
            dec=dec+2**i 
        ip=ip//10  
l=len(dp)         
for i in range(0,l):
    if dp[i]=='1':
        dec += (2**(-(i+1)))
print(dec)