"""WeightStation"""
def main():
    """main"""
    avg = float(input())
    pos1 = float(input())
    pos2 = float(input())
    pos3 = float(input())
    pos4 = 4 * avg - (pos1 + pos2 + pos3)
    halfavg = avg / 2
    if pos1 + pos2 +pos3 + pos4 > 15000:
        print("Overweight")
    elif  not avg - halfavg <= pos1 <= avg + halfavg:
        print("Unbalance")
    elif  not avg - halfavg <= pos2 <= avg + halfavg:
        print("Unbalance")
    elif  not avg - halfavg <= pos3 <= avg + halfavg:
        print("Unbalance")
    elif  not avg - halfavg <= pos4 <= avg + halfavg:
        print("Unbalance")
    else :
        print(f"Pass {pos4:.2f}")
main()
