l1=int(input("Enter the size of the set 1:"))
l2=int(input("Enter the size of the set 2:"))
set1=set()
set2=set()
for i in range(l1):
    set1.add(input("set 1:"))
for i in range(l2):
    set2.add(input("set 2:"))
set3=set1.union(set2)
print("The union of all sets is ",set3)
set4=set1.intersection(set2)
print("The intersection of the two sets is ",set4)
set5=set1.symmetric_difference(set2)
print("Symmetric difference: ",set5)
