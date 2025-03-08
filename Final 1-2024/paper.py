"""paper"""
def main(pa1, pa2):
    """main"""
    size1, size2 = pa1[1:], pa2[1:]
    print(2**(int(size2) - int(size1)))
main(input(), input())
