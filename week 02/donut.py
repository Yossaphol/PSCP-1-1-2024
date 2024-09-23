"""donut"""
import math
def main():
    """main"""
    a = int(input()) #price of donut per piece
    b = int(input()) #buy (piece)
    c = int(input()) #get free (piece)
    d = int(input()) #want (piece)
    if d <= b:
        pay = d * a
        print(pay, d)
    else:
        box = b + c
        count = math.ceil(d / box)
        pay = b * count * a
        ans2 = box * count
        print(pay, ans2)
main()
