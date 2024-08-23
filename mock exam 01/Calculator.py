"""Calculator"""
def cal(n):
    """count button in calculator"""
    if n > 1:
        result = ''
        for i in range(1,n+1):
            result += str(i) + '+'
        ans = len(result)
        print(result)
        print(ans)
    else:
        print(1)
cal(int(input()))
