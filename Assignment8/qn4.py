f1 = open("ip1.txt","r")
str =  f1.readline()
words = str.split(" ")
count = 0
for i in words:
    if len(i) == 4:
        count += 1
print(f"The number of four letter words are {count}")