"""Ticket Fare"""
def main():
    """main"""
    N = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    f = int(input())
    g = int(input())
    paid = 0
    sit1 = 0
    sit2 = 0
    sit = abs(f - g) + 1
    print(sit)
    if sit <= N and sit >= 0:
        if sit <= a:
            paid += b
            sit1 = sit - a
        if sit1 <= c:
            paid += d * sit1
            sit2 = sit1 - c
        if sit2:
            paid += e * sit2
        print(paid)
    else:
        print('Error')
main()
