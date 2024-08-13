"""Run Length Decoding"""
def main():
    """main"""
    txt = input()
    result = ''
    num = ''
    for i in txt:
        if i.isnumeric():
            num += i
        else:
            result += int(num)*i
            num = ''
    print(result)
main()
