"""Diamond I"""
def main():
    """Diamond I"""
    deep = int(input())
    length = int(input())
    diamond = []
    value_daimond = []
    for _ in range(deep):
        value = input().split()
        diamond.append(value)
    for i in range(length):
        cal = 0
        for j in diamond:
            cal += int(j[i])
        value_daimond.append(cal)
    print(max(value_daimond))
main()
