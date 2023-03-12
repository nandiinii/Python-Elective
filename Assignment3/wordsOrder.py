str=input("Enter a sentence:")
words=str.split(" ")
for i in range(len(words)):
    words[i]=words[i].lower()
words.sort()
print(words)
