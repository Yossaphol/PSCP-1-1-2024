"""Sequence I"""
def main():
    """main"""
    num = int(input())
    for _ in range(1,num+1):
        for j in range(1,num+1):
            print(j,end=' ')
        print("")
main()
