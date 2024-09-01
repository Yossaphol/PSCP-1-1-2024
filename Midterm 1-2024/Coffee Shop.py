"""Coffee Shop"""
def promotion(a, b, c, d, e):
    """choose promotion"""
    result1 = a + ((a - (b / 100) * a) * (e - 1))
    result2 = ((a * e) - ((a * e) * (c / 100)))
    if a * e < d:
        print(1)
        print(f'{result1:.2f}')
    else:
        if result1 == result2 or result1 > result2:
            print(2)
            print(f'{result2:.2f}')
        else:
            print(1)
            print(f'{result1:.2f}')
promotion(float(input()), float(input()), float(input()), float(input()), int(input()))
