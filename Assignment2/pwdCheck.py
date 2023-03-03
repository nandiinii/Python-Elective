pwd = input("Enter the password:")
c1=0
c2=0
c3=0
c4=0
for i in range(len(pwd)):
    if pwd[i].isalpha():
        if pwd[i].isupper():
            c1 += 1
        else:
            c2 += 1
    elif pwd[i].isdigit():
        c3 += 1
    elif pwd[i]=='$' or pwd[i] =='#' or pwd[i] == '@':
        c4 += 1
if len(pwd)<8 or c1==0 or c2==0 or c3==0 or c4==0:
    print("Invalid password")
    print("The password is invalid due to the any of the following reasons")
    print("1)Minimum length of password is 8")
    print("2)There should be atleast one character from A-Z,a-z")
    print("3)There should be atleast one special character from the following- @,$ and #")
    print("4)There should be atleast one digit from 0-9")
else:
    print("Valid Password")


