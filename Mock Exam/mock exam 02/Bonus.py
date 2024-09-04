"""Bonus"""
def main(salary, year, month):
    """main"""
    if month >= 10:
        year += 1
    if year >= 20:
        year = 20
    result = salary * year
    if result >= 1000000:
        result = 1000000
    if result <= 5000:
        result = 5000
    print(result)
main(int(input()), int(input()), int(input()))
