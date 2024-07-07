"""EuclideanDistance2D"""
import math
def main():
    """main"""
    pos1 = float(input())
    pos2 = float(input())
    pos3 = float(input())
    pos4 = float(input())
    ans = math.sqrt((pos1 - pos3)**2 + (pos2 - pos4)**2)
    print(ans)
main()
