"""Sequence V"""
def main():
    """main"""
    num = int(input())
    j = 0
    for i in range(num,0,-1):
        print(i,end=' ')
        j += 1
        if not j % 7:
            print()
main()
