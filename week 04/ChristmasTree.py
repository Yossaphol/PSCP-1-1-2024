"""ChristmasTree"""
def main():
    """main"""
    n = int(input())
    t = int(input())
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    for _ in range(t):
        print(" "*(n-2)+"-"*3)
main()
