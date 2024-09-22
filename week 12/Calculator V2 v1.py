"""Calculator V2"""
def main(n):
    """main"""
    result = 0
    if n == 1:
        print(1)
    else:
        for i in range(1,n+1):
            result += len(str(i)) + 1
        print(result)
main(int(input()))
