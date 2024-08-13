'''align'''
def main():
    '''align'''
    size = int(input())
    align = input()
    text = input()
    if align == "left":
        print(text)
    elif align == "right":
        print(f'{text:>{size}}')
    elif align == "center":
        left = (size - (len(text)))
        tmp = left % 2
        left = left // 2 + tmp
        print((" "*left )+ text)
main()
