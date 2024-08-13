"""Sequence xxx"""
def main():
    """main"""
    num = int(input())
    for i in range(num):
        for j in range(num):
            if i == j or j == num - 1 or i == 0 or j == 0 or i == num - 1 or i == num - j - 1:
                print("*",end='')
            else:
                print(" ",end='')
        print()
main()
