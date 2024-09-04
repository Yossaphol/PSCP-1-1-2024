"""restaurant"""
def restaurant(price_a, price_b, percent_c, plus_d):
    '''Restaurant'''
    allprice = price_a + plus_d
    if allprice >= price_b:
        allprice = allprice * percent_c
    if price_a >= price_b:
        price_a = price_a * percent_c
    if price_a < allprice:
        print(f'No {allprice - price_a:.3f}')
    elif price_a > allprice:
        print(f'Yes {price_a - allprice:.3f}')
    else:
        print("Yes")
restaurant(float(input()), float(input()), ((100 - float(input())) / 100), float(input()))
