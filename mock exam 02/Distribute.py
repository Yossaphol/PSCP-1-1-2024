"""Distribute"""
def main(money, child):
    """main"""
    count = 0
    while money >= 8 and child > 0:
        money -= 8
        if money != 4:
            child -= 1
            count += 1
        else:
            money -= 1
            child -= 1
    print(count)
main(int(input()), int(input()))
