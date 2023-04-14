str=input("Enter the string:")
s=dict()
for i in str:
    s[i]=s.get(i,0)+1
    print(s[i])
print(s)