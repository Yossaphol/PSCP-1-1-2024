"""Inflation"""
def main():
    """main"""
    amount = float(input())
    amount2 = amount * 100
    year = int(input())
    result = amount2
    for _ in range(year):
        result += result*0.0381
    ans = int(result)
    print(f"{ans/100:.2f}")
main()
