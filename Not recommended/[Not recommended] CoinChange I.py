"""[Not recommended] CoinChange I"""
def main(num):
    """main"""
    count = 0
    if not num % 11:
        count = num / 11
    elif not num % 7:
        count = num / 7
    else:
        eleven = num // 11
        coin = num - (eleven * 11)
        seven = coin // 7
        coin = coin - (seven * 7)
        count = eleven + seven + coin
    print(int(count))
main(int(input()))
