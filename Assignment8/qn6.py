def containsSublist(mainList,subList):
    sublist_len = len(subList)
    for i in range(len(mainList) - sublist_len + 1):
        if mainList[i:i+sublist_len] == subList:
            return True
    return False
num = int(input("Enter the count for the main list: "))
main_list = []
for i in range(num):
    temp=int(input())
    main_list.append(temp)
num1 = int(input("Enter the count of sublist: "))
sub_list = []
for i in range(num1):
    temp=int(input())
    sub_list.append(temp)
if containsSublist(main_list,sub_list):
    print("True")
else:
    print("False")
