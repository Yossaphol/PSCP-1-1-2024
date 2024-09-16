"""Sequence xxx"""
def main(square, n):
    """main"""
    for i in range(square):
        for _ in range(n):
            for k in range(square):
                if not k or i==square - 1 or i==square - k - 1:
                    print("*",end='')
                elif i==k or k==square - 1 or not i:
                    print("*", end='')
                else:
                    print(" ",end='')
            print(' ',end='')
        print()
main(int(input()), int(input()))
