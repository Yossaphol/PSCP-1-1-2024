"""MAC"""
def main(txt):
    """main"""
    check = '0123456789.:-ABCDEF'
    r = txt[5:9].isalnum() and txt[10:].isalnum()
    if not(len(txt) == 14 or len(txt) == 17):
        print('ERROR')
    else:
        for i in txt:
            if not i in check:
                return print('ERROR')
        if not(txt.count(':')== 5 or txt.count('-') == 5 or txt.count('.') == 2):
            print('ERROR')
        elif txt[2] == ":" and txt[5] == ":" and txt[8] == ":" and\
txt[11] == ":" and txt[14] == ":":
            print("VALID 2")
        elif txt[2] == "-" and txt[5] == "-" and txt[8] == "-" and\
txt[11] == "-" and txt[14] == "-":
            print("VALID 1")
        elif txt[4] == "." and txt[9] == "." and txt[:4].isalnum() and r:
            print("VALID 3")
        else:
            print("ERROR")
main(input().upper())
