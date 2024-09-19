"""Century"""
def main(n):
    """main"""
    for _ in range(n):
        century = input()
        if century[:4] == 'B.E.':
            number = int(century[5:]) - 543
            if number < 0:
                print('ERROR')
            else:
                result = (number - 1) // 100 + 1
                print(result)
        else:
            number = int(century[5:])
            result = (number - 1) // 100 + 1
            print(result)
main(int(input()))
