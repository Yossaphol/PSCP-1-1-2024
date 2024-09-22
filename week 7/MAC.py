"""MAC"""
def main(txt,a='-',b=':',c='.'):
    """main"""
    check = '0123456789.:-ABCDEF'
    new = ''
    d = not(len(new) == 17 or len(new) == 14)
    e = not (new.count('-') == 5 or new.count(':') == 5 or new.count('.') == 2)
    for i in txt:
        if i in check:
            new += i
        else:
            new += ''
    if d or e:
        print("ERROR1")
    if e:
        print('ERROR2')
    elif new == txt:
        if new[2]==a and new[5]==a and new[8]==a and new[11]==a and new[14]==a:
            print('VALID 1')
        elif new[2]==b and new[5]==b and new[8]==b and new[11]==b and new[14]==b:
            print('VALID 2')
        elif new[4] == c and new[9]==c:
            print('VALID 3')
        else:
            print('ERROR')
    else:
        print('ERROR')
main(input().upper())
