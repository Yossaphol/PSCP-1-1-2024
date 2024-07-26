"""Sequence IV"""
def main():
    """main"""
    n = 1
    num = int(input())
    for _ in range(num):
        for j in range(n,num+n):
            print(j,end=' ')
            n+=1
        print()
main()
