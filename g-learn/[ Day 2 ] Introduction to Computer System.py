"""[ Day 2 ] Introduction to Computer System"""
def main(a, b, c, d=0):
    """main"""
    if c == 1 and b == 0:
        d = 1
    if a == 1 or d == 1:
        print('True')
    else:
        print('False')
main(int(input()), int(input()), int(input()))
