"""Helloooo"""
def main(txt):
    """main"""
    reversed_txt = txt[::-1]
    last = ''
    delete = ''
    length = len(txt) - 1
    check = False
    for i in reversed_txt:
        if i in 'aeiou':
            last += i
            check = True
            break
        else:
            delete += i
            length -= 1
    delete = delete[::-1]
    fisrt = txt[0:length]
    if check:
        print(f'{fisrt}{last*3}{delete}')
    else:
        print(delete)
main(input())
