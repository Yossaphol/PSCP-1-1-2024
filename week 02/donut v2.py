"""donut v2"""
import math
def main():
    """main"""
    a = int(input()) #price of donut per piece
    b = int(input()) #buy (piece)
    c = int(input()) #get free (piece)
    d = int(input()) #want (piece)
    if d < b:
        pay = d * a
        print(pay, d)
    else:
        box = b + c
        set_ = d // box
        if box * set_ == d:
            pay = b * set_ * a
            ans2 = d
        else:
            left = d - (set_ * box)
            pay = (b * set_ * a) + (left * a)
            ans2 = box * set_ + left
        print(pay, ans2)
main()
