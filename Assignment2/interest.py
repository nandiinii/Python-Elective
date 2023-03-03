startBal = float(input("Enter the principal amount:"))
time = int(input("Enter the time in years:"))
rate = int(input("Enter the rate percent:"))
print("Year \t Starting Bal \t Interest \t Ending bal")
sum=0
for i in range(1,time+1):
    interest = round(startBal*0.01*rate,2)
    sum += interest
    endBal = startBal+interest
    print(str(i)+"\t"+str(startBal)+"\t\t"+str(interest)+"\t\t"+str(endBal))
    startBal=endBal
print("The ending balance is {}".format(startBal))
print("The sum of interest is {}".format(sum))