from math import *
def meanList(l,num): 
    sum=0
    for i in range(len(l)):
        sum += l[i]
    mean = round(sum/num,2)
    return mean
def medianList(l,num):
    l.sort()
    print(l)
    mid=num//2
    median=0
    if(num%2==1):
        median=l[mid]
    else:
        median = (l[mid]+l[mid-1])/2
    return median
def modeList(l):
    frequency = {}
    max_count = 0
    modes = []
    for num in l:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

        if frequency[num] > max_count:
            max_count = frequency[num]
    for num, count in frequency.items():
        if count == max_count:
            modes.append(num)
    return modes
num = int(input("Enter the count:"))
l=[]
for i in range(num):
    temp=int(input())
    # val=int(temp)
    l.append(temp)
mean = meanList(l,num)
print(f"Mean: {mean}")
median = medianList(l,num)
print(f"Median: {median}")
mode = modeList(l)
print(f"Mode: {mode}")
