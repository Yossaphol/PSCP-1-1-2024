"""BrickBridge"""
def main():
    """main"""
    small = int(input())
    large = int(input())
    goals = int(input())
    length = (5 * large) + small
    uselarge = goals // 5
    if length >= goals:
        if uselarge > large:
            uselarge = large
        ans = goals - (uselarge * 5)
        if small >= ans:
            print(ans)
        else:
            print(-1)
    else:
        print(-1)
main()
