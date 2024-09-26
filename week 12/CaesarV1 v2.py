"""CaesarV1"""
def main(num, txt):
    """main"""
    up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    low = 'abcdefghijklmnopqrstuvwxyz'
    new = ''
    if num > 26:
        num = num % 26
    for i in txt:
        if i in (' ','.'):
            if i == ' ':
                new += ' '
            else:
                new += '.'
        if i in up:
            char = up.find(i) + num
            if char > len(up):
                char = 0
                char += num
            elif char < 0:
                char = 26
                char += num
            new += up[char]
        if i in low:
            char = low.find(i) + num
            if char > len(low):
                char = 0
                char += num
            elif char < 0:
                char = 26
                char += num
            new += low[char]
    print(new)
main(int(input()),input())
