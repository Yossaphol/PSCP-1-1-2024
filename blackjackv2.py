"""blackjack"""
def main():
    """main"""
    cards = int(input())
    result = 0
    ace = 0
    for _ in range(cards):
        num = input()
        for i in num:
            if i == 'A':
                ace += 1
        if num.isnumeric() or num == '10':
            result += int(num)
        elif num in ['J','Q','K']:
            result += 10

    if ace == 1:
        if result <= 10:
            result += 11
        else:
            result += 1
    elif ace == 2:
        if result < 10:
            result += 12
        else:
            result += 2
    elif ace == 3:
        result += 13
    print(result)
main()
