"""Kapreka"""
def noimak(num):
    """sort number"""
    if len(num) < 4:
        num += '0'
    num1, num2 , num3, num4 = num[0], num[1], num[2], num[3]
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if num3 > num4:
        num3, num4 = num4, num3
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if num3 > num4:
        num3, num4 = num4, num3
    if num1 > num2:
        num1, num2 = num2, num1
    asc = num1 + num2 + num3 + num4
    dec = num4 + num3 + num2 + num1
    return dec, asc
def main(number):
    """main"""
    count = 0
    while number != 6174:
        dec, asc = noimak(str(number))
        number = int(dec) - int(asc)
        count += 1
    print(count)
main(int(input()))
