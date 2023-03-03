print("Enter the three sides of a triangle")
a=int(input("First:"))
b=int(input("Second:"))
c=int(input("Third:"))
arr = (a,b,c)
x = sorted(arr)
if (x[2]**2 == x[0]**2+x[1]**2):
    print("Right Angled Triangle")
else:
    print("Not a right angled triangle")


