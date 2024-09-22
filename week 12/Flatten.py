"""Flatten"""
import json
def main(txt):
    """main"""
    x = len(txt)
    new = ''
    pro = ''
    for i in txt[1:x-1]:
        new += i
    for i in new:
        if i in ('[',']'):
            pro += ''
            continue
        pro += i
    final = '[' + pro + ']'
    a = json.loads(final)
    a.sort(reverse = True)
    print(a)
main(input())
