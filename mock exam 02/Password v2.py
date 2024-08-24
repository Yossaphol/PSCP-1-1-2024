"""Password"""
import math
def main(txt):
    """main"""
    l = len(txt)
    R = 0
    lower = 0
    upper = 0
    num = 0
    special = 0
    for i in txt:
        if i.islower():
            lower = 26
        if i.isupper():
            upper = 26
        if i.isnumeric():
            num = 10
        if i.isprintable():
            special = 32
    R = lower + upper + num + special
    E = int(math.log(R**l,2))
    print(E)
    if E < 28:
        print('Very Weak')
    elif 28 <= E <= 35:
        print("Weak")
    elif 36 <= E <= 59:
        print("Reasonable")
    elif 60 <= E <= 127:
        print("Strong")
    else:
        print("Very Strong")
main(input())
