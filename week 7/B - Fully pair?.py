"""B - Fully pair?"""
def main(txt):
    """main"""
    result = ''
    for i in txt:
        if txt.count(i)%2 == 0:
            txt = txt.replace(i,'')
        else:
            x = txt.count(i)
            y = (x // 2) * 2
            txt = txt.replace(i,'',y)
    result = txt
    if result == '':
        print('fully paired')
    else:
        print(result)
main(input())
