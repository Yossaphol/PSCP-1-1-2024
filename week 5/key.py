"""key"""
def main():
    """main"""
    txt = input()
    total = 0
    for i in txt:
        num = int(i)
        total += num
    total += int(txt[-3:]) * 10
    if total < 1000:
        total += 1000
    elif total > 9999:
        total = str(total)
        total = total[-4:]
    print(total)
main()
