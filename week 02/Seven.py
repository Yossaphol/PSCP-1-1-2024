"""Seven"""
def main():
    """main"""
    num = int(input())
    if not num % 4:
        print(0)
    elif num % 4 == 1:
        print(7)
    elif num % 4 == 2:
        print(9)
    elif num % 4 == 3:
        print(3)
main()
