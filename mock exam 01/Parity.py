"""Parity"""
def main():
    """odd even bit"""
    txt = input()
    typeoe = input()
    if typeoe == 'Odd':
        if txt.count('1') % 2 == 1:
            txt += '0'
        else:
            txt += '1'
    else:
        if not txt.count('1') % 2:
            txt += '0'
        else:
            txt += '1'
    print(txt)
main()
