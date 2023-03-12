print("Enter the 10 numbers in a tuple")
num=()
for i in range(0,10):
    x=(int(input()),)
    num+=x
sum=0
avg=0.0
print("The minimum value is {}".format(min(num)))
print("The maximum value is {}".format(max(num)))
for i in range(len(num)):
    sum += num[i]
print("The sum is {}".format(sum))
avg=round(sum/10,2)
print("Average:",avg)
