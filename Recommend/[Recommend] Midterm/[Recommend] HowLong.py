"""HowLong"""
def main():
    """Entry"""
    num = input()
    num = str(abs(int(num)))
    ount = 0
    for _ in num:
        ount += 1
    print(ount)
main()
