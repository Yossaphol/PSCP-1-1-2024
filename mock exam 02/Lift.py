"""Lift"""
def main(n, liftweight):
    """main"""
    baby = 1
    weightall = 0
    for _ in range(n):
        age = int(input())
        weight = float(input())
        if age >= 12:
            baby = 0
        weightall += weight
    if not n:
        print('Safe')
    else:
        if baby == 1 or weightall > liftweight:
            print('Not Safe')
        else:
            print('Safe')
main(int(input()), float(input()))
