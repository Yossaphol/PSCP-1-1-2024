"""mathforit"""
import math
def main():
    """main"""
    rad = float(input())
    area = math.pi * (rad **2)
    cir = 2 * math.pi * rad
    print(f"Area: {area:.3f}")
    print(f"Circumference: {cir:.3f}")
main()
