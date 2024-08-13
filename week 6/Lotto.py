"""Lotto"""
def main():
    """Main Function"""
    winning = input()
    lasts2 = input()
    front3 = input()
    front3_2 = input()
    lasts3 = input()
    lasts3_2 = input()
    numlotto = input()
    result = 0
    if numlotto == winning:
        result += 6000000
    if numlotto.endswith(lasts2):
        result += 2000
    if numlotto[0:3] == front3:
        result += 4000
    if numlotto[0:3] == front3_2:
        result += 4000
    if numlotto.endswith(lasts3):
        result += 4000
    if numlotto.endswith(lasts3_2):
        result += 4000
    if winning == '000000':
        if numlotto in ('000001', '999999'):
            result += 100000
    if winning == '999999':
        if numlotto in ('999998', '000000'):
            result += 100000
    if int(numlotto) in (int(winning) + 1, int(winning) - 1) and\
        not numlotto in ('000001', '999999', '999998', '000000'):
        result += 100000
    print(result)
main()
