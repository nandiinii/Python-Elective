lst=[2,5.67,"Python","Elective",4,6.54,3.21,3]
integer=[]
floating=[]
string=[]
for i in range(len(lst)):
    if type(lst[i])==int:
        integer.append(lst[i])
    elif type(lst[i])==float:
        floating.append(lst[i])
    if type(lst[i])==str:
        string.append(lst[i])
print("Integer List: ",integer)
print("Float Values List: ",floating)
print("Strings List: ",string)

