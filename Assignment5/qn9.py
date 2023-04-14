def dectobin(n):
    return bin(n)[2:].zfill(4)

def bcd(n):
    bcdstr= ''
    for digit in str(n):
        bcdstr += dectobin(int(digit))
    return bcdstr
num = 274
bcdnum=bcd(num)
print("The BCD representation of {} is {}".format(num,bcdnum))