str=input("Enter the string:")
words=str.split(" ")
length=0
for i in range(len(words)):
    print(words[i])
for i in range(len(words)):
    length += len(words[i])
    print("The length of {} is {}".format(words[i],len(words[i])))
avg = length/len(words)
print("Average:",round(avg,2))