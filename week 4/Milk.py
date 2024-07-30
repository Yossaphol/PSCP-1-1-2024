"""Milk"""
def main():
    """main"""
    a = float(input())
    b = int(input())
    c = int(input())
    d = float(input())
    bottle = d // a
    promotion = bottle // b
    sumpromotion = promotion * c
    result = bottle + sumpromotion
    print(int(result))
main()
