"""Parallelogram"""
def main():
    """main"""
    txt = input()
    i = 0
    space = len(txt) - 1
    while i < len(txt):
        print(' '*space+txt[0:i+1])
        space -= 1
        i += 1
    j = len(txt)
    while j > 1:
        print(txt[-j+1:])
        j -= 1
main()
