"""coke"""
def coke(price, lid, newprice, wanted):
    """less price"""
    if not lid:
        result = price * wanted
    else:
        discount = int((wanted - 1) / lid)
        result = (discount * newprice) + ((wanted - discount) * price)
    print(result)
coke(int(input()), int(input()), int(input()), int(input()))
