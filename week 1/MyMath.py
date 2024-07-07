"""mymath"""
import math
def main():
    """mymath"""
    line1 = (math.sin(math.radians(90))+(math.sin(math.radians(60)))**2)
    line2 = (math.cos(math.radians(245**2))+(math.cos(math.radians(45+135))))
    print(line1/line2)
    print(math.factorial(16)*(math.factorial(4))/math.factorial(8))
    print(40/math.sqrt(((25-12)**2)+(12-15)**2))
    print(math.log10(1234**4))
    line3 = (math.log(4234,5)+math.log2(8191)+71*(math.log10(156154)))
    line4 = (math.log(777,7)-math.log(888,8)-(math.log(999,9)))
    print(line3/line4)
main()
