"""bank"""
inbank = float(input())
pocket = float(input())

while True:
    income = input()    
    if income == 'end':
        break
    checkdw = income[0]
    money = float(income[2:])
    error = 0
    if error == 3:
        break
    else:
        if checkdw == 'D':
            if pocket < money:
                error += 1
                continue
            else :
                inbank += money
                pocket -= money
        elif checkdw == 'W':
            if inbank < money:
                error += 1
                continue
            else :
                inbank -= money
                pocket += money
print(f"{inbank:.2f}")
print(f"{pocket:.2f}")