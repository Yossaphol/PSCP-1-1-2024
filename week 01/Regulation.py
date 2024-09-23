"""Regulatio"""
def main():
    """Regulatio"""
    aaa = int(input())
    bbb = float(input())
    ccc = str(input())
    print(f"{aaa:>30}")
    if aaa < 0:
        print(f"-{abs(aaa):>029}")
    else:
        print(f"{aaa:>030}")
    print(f"{bbb:.2f}")
    print(f"{bbb:.12f}")
    print(f"{ccc:>40}")
main()
