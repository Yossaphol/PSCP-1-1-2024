"""Inverter"""
def main(num):
    """main"""
    new = ''
    for i in num:
        if i == '0':
            new += '1'
        else:
            new += '0'
    if not int(new):
        print()
    else:
        print(int(new))
main(input())
