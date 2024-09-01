"""Number Message"""
def word(txt):
    """return num to alpha"""
    txt = txt.replace('13', 'B')
    txt = txt.replace('12', 'R')
    new = ''
    for i in txt:
        if i == '1':
            new += 'I'
        elif i == '3':
            new += 'E'
        elif i == '4':
            new += 'A'
        elif i == '5':
            new += 'S'
        elif i == '0':
            new += 'O'
        else:
            if i.isalpha() or i == ' ':
                new += i
    print(new)
word(input().upper())
