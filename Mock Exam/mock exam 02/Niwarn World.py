"""Niwarn World"""
import math
def x(n):
    """x"""
    return 2 + (math.log(n**2)/(2*n*math.log(n)))
def y(n, s):
    """y"""
    return (math.sin(math.radians(30)) + math.sqrt(2*s)) / (x(n)+3)
def z(k):
    """z"""
    return (y(k,k))**2+((8456 * (x(k))**4)/(24*k))
def main(n, s, k):
    """main"""
    print(f'X: {x(n):.1f}, Y: {y(n, s):.1f}, Z: {z(k):.1f}')
main(float(input()), float(input()), float(input()))
