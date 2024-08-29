"""Pringles"""
def main():
    """main"""
    size1 = input()
    amount = input()
    size2 = input()
    eat = int(input())
    count = 0
    check = len(amount) - 1
    if eat > len(size1):
        print(eat)
        print("None.")
        print(size1)
        print(len(size1)*" "+"|")
        print(size2)
    else:
        i = 0
        while i < eat:
            if amount[i] == ')':
                count += 1
            i += 1
        pringles = amount[eat:check]
        print(count)
        if pringles.find(')') == -1:
            print("None.")
        else:
            print("There are still some left.")
        print(size1)
        print(' '*eat + pringles + '|')
        print(size2)
main()
