"""XI"""
def main(num):
    """main"""
    size = (2 * num) - 1
    for i in range(1,size+1):
        for j in range(1,size+1):
            check = min(i, j, size-j+1, size-i+1)
            print(f"{check:02}",end=' ')
        print()
main(int(input()))
