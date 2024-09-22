"""Divide3Or5"""
def main():
    """main"""
    n = int(input())
    result = 0
    for i in range(n+1):
        if not i % 3 or not i % 5:
            result += i
    print(result)
main()
