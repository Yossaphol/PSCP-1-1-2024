"""coke"""
def coke():
    """less price"""
    bottle = int(input())
    change = int(input())
    newprice = int(input())
    want = int(input())
    lid = 0
    price = 0
    coke = 0
    while coke < want:
        price += bottle
        coke += 1
        lid += 1
        if lid == change:
            bottle = newprice
        else:
            bottle = bottle
    print(price)
coke()
