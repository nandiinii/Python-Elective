str=input("enter the string")
word=str.split(" ")
d=dict()
for i in word:
    d[i]=d.get(i,0)+1
    print(d[i])
print(d)
print("words with maxm frequency:")
maxm=max(d.values())
for i in d:
    if maxm==d[i]:
        print(i)


        


