"""CoinChangeV1"""
def main(num):
    """main"""
    twentyfive = num // 25
    coin = num - (twentyfive * 25)
    ten = coin // 10
    coin1 = coin - (ten * 10)
    five = coin1 // 5
    coin2 = coin1 - (five * 5)
    print(coin2 + twentyfive + ten + five)
main(int(input()))
