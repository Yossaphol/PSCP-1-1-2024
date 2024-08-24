"""Bad Keyboard"""
def main():
    """main"""
    txt = input()
    new = ''
    for i in txt:
        if i == 'o':
            i = 'i'
            new += i
            continue
        if i == 'i':
            i = 'o'
            new += i
            continue
        if i == 'I':
            i = 'O'
            new += i
            continue
        if i == 'O':
            i = 'I'
            new += i
            continue
        new += i
    print(new)
main()
