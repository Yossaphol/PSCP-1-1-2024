"""donut"""
def main():
    """main"""
    a = int(input()) #price of donut per piece
    b = int(input()) #buy (piece)
    c = int(input()) #get free (piece)
    d = int(input()) #want (piece)
    box = b + c
    count = d // box
    count1 = d % box
    if count1 > 0:
        count += 1
    pay = b * count * a
    ans2 = box * count
    print(pay, ans2)
main()
