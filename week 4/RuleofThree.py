"""RuleofThree"""
def main():
    """main"""
    n = int(input())
    lessprice = 0
    lessweight = 0
    perbaht1 = 0
    for _ in range(n):
        price = float(input())
        weight = float(input())
        perbaht = weight / price
        if perbaht1 == weight / price:
            perbaht1 = perbaht
        elif perbaht1 < weight / price:
            perbaht1 = perbaht
            lessprice = price
            lessweight = weight
    print(f"{lessprice:.2f} {lessweight:.2f}")
main()
