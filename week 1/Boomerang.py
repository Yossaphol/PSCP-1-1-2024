"""boomerang"""
import math
def main():
    """main"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    print(num1 + 1)
    print(7*num2**3 + 2*num2**2-31*num2+1)
    print(-num3)
    print((num1 + num2) * (num1 - num2))
    print((num2 - math.sqrt((num2**2) - (4 * num1 * num3)))/ (2 * num1))
main()
