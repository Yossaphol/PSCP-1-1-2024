"""ham"""
def main():
    """main"""
    left = int(input())
    right = int(input())
    meat = 2 * (left + right)
    print("|"*left + "*"*meat + "|"*right)
main()
