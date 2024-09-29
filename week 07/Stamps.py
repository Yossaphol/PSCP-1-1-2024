"""Stamps"""
def main(n, a, b, c, d):
    """main"""
    stamps = 0
    for _ in range(n):
        price = int(input())
        x = a // price
        stamp = x * b
        stamps += stamp
    #not pass  
main(int(input()), int(input()), int(input()), int(input()), int(input()))
