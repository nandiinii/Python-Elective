num= int(input("Enter the count of students"))
l1=list()
for i in range(0,num):
    temp=input()
    l1.append(temp)
l1.sort()
print(l1)
val=0
for i in range(1,len(l1)):
    if len(l1[val])<len(l1[i]):
        val=i
print("The name with maximum length is:{}".format(l1[val]))
print("Names starting with 'A' are")
for i in range(len(l1)):
    if l1[i][0]=="A":
        print(l1[i])
    l1[i]=l1[i].upper()
l1.reverse()
print("The reverse list:{} ".format(l1))
l1.sort(key=len)
print("The sorted list according to length:{} ".format(l1))


    
    





    

