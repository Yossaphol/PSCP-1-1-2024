"""BlackJack"""
def main():
    """main"""
    num = int(input())
    result = 0
    ace = 0
    for _ in range(num):
        card = input()
        if card.isnumeric():
            result += int(card)
        elif card in ['J','Q','K']:
            result += 10
        elif card == "A":
            ace += 1
    if ace == 1:
        if result <= 10:
            result += 11
        else:
            result += 1
    elif ace == 2:
        if result < 10:
            result += 12
        else :
            result += 2
    elif ace == 3:
        result += 13
    print(result)
main()
