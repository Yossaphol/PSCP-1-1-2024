"""Ball"""
def main():
    """main"""
    i = -1
    check = True
    height = float(input())
    while check:
        height *= 3/5
        if height < 0.01:
            check = False
        i += 1
    print(i)
main()
