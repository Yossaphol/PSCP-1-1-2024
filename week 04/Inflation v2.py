"""inflation"""
def main(price, year):
    """main"""
    price *= 100
    price = int(price)
    for _ in range(year):
        price += (price*381)//10000
    print(f"{int(price//100):d}.{int(price%100):02d}")
main(float(input()),int(input()))
