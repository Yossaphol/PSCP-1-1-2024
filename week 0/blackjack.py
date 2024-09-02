"""blackjack"""
def main():
    """main"""
    num = int(input())
    result = 0
    for _ in range(num):
        card = input()
        if card.isnumeric() or card == '10':
            result += int(card)
        elif card in ('J', 'Q', 'K'):
            result += 10
        elif card == 'A':
            if result < 21:
                result += 11
                if result > 21:
                    result -= 10
            else:
                if num == 3:
                    result += 1
                    result -= 10
                else :
                    result += 1
    print(result)
main()
