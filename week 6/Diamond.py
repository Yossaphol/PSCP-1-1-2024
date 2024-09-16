"""Diamond"""
def main(n):
    """main"""
    m = n // 2
    for i in range(m):
        print(' ' * (m - i) + '*' + ' ' * (2 * i - 1) + ('*' if i > 0 else ''))
    print('*' * n)
    for i in range(m-1, -1, -1):
        print(' ' * (m - i) + '*' + ' ' * (2 * i - 1) + ('*' if i > 0 else ''))
main(int(input()))
