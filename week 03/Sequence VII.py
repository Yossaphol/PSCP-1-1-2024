"""Sequence VII"""
def main():
    """main"""
    num = int(input())
    for i in range(1,num+1):
        for j in range(1,num+1):
            if j <= i:
                print(j,end=' ')
            else:
                print('',end='')
        print()
    for i in range(num-1,0,-1):
        for j in range(1,num):
            if j <= i:
                print(j,end=' ')
            else:
                print('',end='')
        print()
main()
