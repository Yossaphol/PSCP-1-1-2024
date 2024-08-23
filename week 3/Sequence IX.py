"""ix"""
def main(num):
    """main"""
    for i in range(1,num+1):
        for _ in range(num-i):
            print("  ",end=' ')
        for j in range(1,i+1):
            print(f"{j:>02}",end=' ')
        for j in range(j-1,0,-1):
            print(f"{j:>02}",end=' ')
        print()
main(int(input()))
