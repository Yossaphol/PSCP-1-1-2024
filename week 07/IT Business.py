"""IT"""
def main():
    """bank"""
    inbank = float(input())
    pocket = float(input())
    error = 0
    while True:
        income = input()
        if income == 'end':
            break
        checkdw = income[0]
        money = float(income[2:])
        if checkdw == 'D':
            if pocket < money:
                error += 1
            else :
                inbank += money
                pocket -= money
                error = 0
        elif checkdw == 'W':
            if inbank < money:
                error += 1
            else :
                inbank -= money
                pocket += money
                error = 0
        if error == 3:
            break
    print(f"{inbank:.2f}")
    print(f"{pocket:.2f}")
main()
