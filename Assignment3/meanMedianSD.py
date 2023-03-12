from math import *
num = int(input("Enter the count:"))
l=[]
for i in range(num):
    temp=input()
    val=int(temp)
    l.append(val)
sum=0
for i in range(len(l)):
    sum += l[i]
mean = round(sum/num,2)
print("Mean:",mean)
l.sort()
print(l)
mid=num//2
median=0
if(num%2==1):
    median=l[mid]
else:
    median = (l[mid]+l[mid-1])/2
print("The median is ",median)
sum=0
for i in range(len(l)):
    sum += (l[i]-mean)**2
sd= sqrt(round(sum/num,2))
print("Standard Deviation:",round(sd,2))
