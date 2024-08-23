"""Milk"""
def main():
    """main"""
    price = float(input())
    lid = int(input())
    free = int(input())
    wallet = float(input())
    if not lid:
        amount = wallet // price
        print(int(amount))
    else:
        box = lid * price
        amount = wallet // box
        result = (lid + free) * amount
        print(int(result))
main()
