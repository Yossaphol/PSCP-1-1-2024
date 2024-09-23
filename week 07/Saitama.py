"""saitama"""
import math
def main():
    """main"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    daya = int(input())
    dayb = int(input())
    dayd = int(input())
    dayc = int(input())
    n = 0
    if n < a / daya:
        n = a / daya
    if n < b / dayb:
        n = b / dayb
    if n < c / dayc:
        n = c / dayc
    if n < d / dayd:
        n = d / dayd
    print(math.ceil(n))
main()
