"""BrickBridge"""
def main():
    """main"""
    small = abs(int(input()))
    large = abs(int(input()))
    goal = int(input())
    check = 0
    result = 0
    if small + large * 5 >= goal:
        if large * 5 < goal:
            check += (large * 5)
        elif large * 5 >= goal:
            large -= 1
            check += (large * 5)
        checksmall = goal - check
        if small < checksmall:
            print(-1)
        else:
            i = 0
            while i < checksmall:
                result += 1
                i += 1
            print(result)
    else:
        print(-1)
main()
