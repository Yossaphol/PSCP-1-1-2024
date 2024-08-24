"""Longer"""
import math
def main(r, a, b):
    """main"""
    areac = 2 * math.pi * r
    arear = 2 * (a + b)
    if areac > arear:
        print('Circle is longer')
    elif arear > areac:
        print('Rectangle is longer')
    else:
        print('Equal')
    print(f'{abs(areac - arear):.5f}')
main(float(input()), float(input()), float(input()))
