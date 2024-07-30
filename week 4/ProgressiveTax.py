"""ProgressiveTax"""
def main():
    """tax tax"""
    income = int(input())
    tax = 0
    if income > 4000000 :
        income -= 4000000
        tax += income * 0.35
        income = 4000000
    if 2000001 <= income <= 4000000:
        income -= 2000000
        tax += income * 0.3
        income = 2000000
    if 1000001 <= income <= 2000000:
        income -= 1000000
        tax += income * 0.25
        income = 1000000
    if 750001 <= income <= 1000000:
        income -= 750000
        tax += income * 0.2
        income = 750000
    if 500001 <= income <= 750000:
        income -= 500000
        tax += income * 0.15
        income = 500000
    if 300001 <= income <= 500000:
        income -= 300000
        tax += income * 0.1
        income = 300000
    if 150001 <= income <= 300000:
        income -= 150000
        tax += income * 0.05
        income = 150000
    if income < 150000:
        tax = 0
    print(f"{int(tax)}")
main()
