"""Post Office"""
def envelop(weight):
    """envelop"""
    price = 0
    if 0 <= weight <= 10:
        price = 16
    elif 10 < weight <= 20:
        price = 18
    elif 20 < weight <= 100:
        price = 23
    elif 100 < weight <= 250:
        price = 28
    elif 250 < weight <= 500:
        price = 33
    elif 500 < weight <= 1000:
        price = 48
    elif 1000 < weight <= 2000:
        price = 68
    return  price
def package(weight):
    """package"""
    price = 0
    if 0 <= weight <= 500:
        price = 45
    elif 500 < weight <= 1000:
        price = 55
    elif 1000 < weight <= 2000:
        price = 70
    return price
def stamp(n, m):
    """post office"""
    result = 0
    for _ in range(n):
        result += envelop(float(input())) + 13
    for _ in range(m):
        result += package(float(input())) + 15
    print(result)
stamp(int(input()), int(input()))
