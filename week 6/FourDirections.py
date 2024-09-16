"""FourDirections"""
def main(pattern):
    """UDLR"""
    pat_U = [
        '  *  ',
        ' *** ',
        '* * *',
        '  *  ',
        '  *  '
    ]
    pat_D = [
        '  *  ',
        '  *  ',
        '* * *',
        ' *** ',
        '  *  '
    ]
    pat_L = [
        '  *  ',
        ' *   ',
        '*****',
        ' *   ',
        '  *  '
    ]
    pat_R = [
        '  *  ',
        '   * ',
        '*****',
        '   * ',
        '  *  '
    ]
    for i in range(5):
        for j in pattern:
            if j == 'U':
                print(pat_U[i], end=' ')
            elif j == 'D':
                print(pat_D[i], end=' ')
            elif j == 'L':
                print(pat_L[i], end=' ')
            elif j == 'R':
                print(pat_R[i], end=' ')
        print()
main(input())
