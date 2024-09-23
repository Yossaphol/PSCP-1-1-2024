"""x"""
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
    for a in range(num,1,-1):
        for _ in range(num-a+1):
            print("  ",end=' ')
        for b in range(1,a):
            print(f"{b:>02}",end=' ')
        for b in range(a-2,0,-1):
            print(f"{b:>02}",end=' ')
        print()
main(int(input()))
