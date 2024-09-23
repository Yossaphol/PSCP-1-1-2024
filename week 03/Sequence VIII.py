"""Sequence VIII"""
def main():
    """main"""
    num = int(input())
    for i in range(1,num+1):
        tem = 0
        for j in range(1,num+1):
            if  i > ((num) - j):
                tem += 1
                print(f"{tem:>02}", end=' ')
            else:
                print("  ",end=' ')
        print()
main()
