def maxm(*args):
    maxnum=args[0]
    for num in args:
        if num>maxnum:
            maxnum=num
    return maxnum
print(maxm(4,2,6,7,129,12,45))