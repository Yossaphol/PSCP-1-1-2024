"""Cha Cha Cha"""
import math
def main():
    """doc"""
    day = int(input())
    total = 0
    for _ in range(day):
        hour = math.ceil(float(input()))
        total += hour * 8720
    print(total)
main()
