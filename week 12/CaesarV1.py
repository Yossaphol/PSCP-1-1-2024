"""CaesarV1"""
def main(num, txt):
    """main"""
    new = ''
    if num > 26:
        num = num % 26
    for i in txt:
        if i == ' ' or i == '.':
            if i == ' ':
                new += ' '
            else:
                new += '.'
        else:
            x = ord(i)
            y = x + num
            if i.isupper() and y < 65:
                y = 90
                y = x + num
            elif i.isupper() and y > 90:
                y = 65
                y = x + num
            elif i.islower() and y > 122:
                y = 122
                y = x + num
            elif i.islower() and y < 97:
                y = 122
                y = x + num
            new += chr(y)
    print(new)
main(int(input()),input())
