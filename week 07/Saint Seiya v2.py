"""Saint Seiya v2"""
def main(sec, punch):
    """main"""
    result = 0
    for i in range(2,sec+1,2):
        if result < punch:
            if not i % 6:
                result += 1
            elif not i % 2:
                result += 165
        else:
            result += (sec + 1 - i) * 12
            break
    print(result)
main(int(input()), int(input()))
