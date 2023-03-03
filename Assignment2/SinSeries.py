n=int(input("Enter the n value:"))
sine=""
j=0
for i in range(1,n+1,2):
    if j%2 == 0 and i!=n and i!=n-1:
        sine = sine + ("(x^"+str(i)+"/"+str(i)+"!)-")
    elif j%2!=0 and i!=n and i!=n-1:
        sine = sine + ("(x^"+str(i)+"/"+str(i)+"!)+")
    elif i==n or i==n-1:
        sine = sine + ("(x^"+str(i)+"/"+str(i)+"!)")
    j=j+1
print(sine)
