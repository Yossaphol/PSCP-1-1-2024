"""Parity"""
def main():
    """odd even bit"""
    txt = input()
    typeoe = input()
    one = 0
    for i in txt:
        if txt[i] == '1':
            one += 1
    if typeoe == 'Odd':
        if one % 2 == 1:
            txt += '0'
        else:
            txt += '1'
    else:
        if not one % 2:
            txt += '0'
        else:
            txt += '1'
    print(txt)
main()
