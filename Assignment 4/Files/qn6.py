from collections import Counter
f1=open("txt5.txt","r")
str=f1.read()
str=str.replace("\n","")
words=str.split(" ")
cnt=Counter(words)
maxm=0
word=""
for i in cnt:
    if cnt[i]>maxm:
        maxm=cnt[i]
        word=i
print("Most Frequent word is '{}'".format(word))
f1.close()