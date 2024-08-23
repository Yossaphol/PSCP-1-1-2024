"""Heron of Alexandria"""
import math
def heron(a, b, c):
    """find area"""
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(f"{area:.3f}")
heron(float(input()), float(input()), float(input()))
