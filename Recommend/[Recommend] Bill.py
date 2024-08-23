"""Bill"""
def main():
    """main"""
    cost = int(input())
    pay = cost * 0.1
    if pay < 50:
        pay = 50
    if pay > 1000:
        pay = 1000
    vat = cost + pay
    result = vat + (vat *0.07)
    print(f"{result:.2f}")
main()
