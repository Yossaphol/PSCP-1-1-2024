"""Shorten"""
def main():
    """main"""
    i = 1
    Set = '1'
    while True:
        num = int(input())
        if num == -1:
            break
        if num == i:
            i += 1
        else:
            Set += str(num) + '-'
        Set += str(num)
main()
