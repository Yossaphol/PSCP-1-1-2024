"""Saint Seiya"""
def main(sec, punch):
    """main"""
    result = 0
    i = 1
    check = 0
    while i <= sec:
        if result < punch:
            if not i % 6:
                result += 1
                i += 1
            elif not i % 2:#even
                result += 165
                i += 1
            else:
                i += 1
        else:
            if not check:
                i += 1
                check += 1
                continue
            result += 12
            i += 1
    print(result)
main(int(input()), int(input()))
