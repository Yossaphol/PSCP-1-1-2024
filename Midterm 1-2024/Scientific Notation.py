"""scientific notation"""
def main(num):
    """main"""
    fill = ''
    s3t = ''
    count = 0
    indexpoint = 0
    power = 0
    indexpower = 0
    if num.find('x') == -1:
        if num.find('.') == -1:
            ren = len(num) - 1
            number = int(num) / (10**ren)
            print(f'{number} x 10^{ren}')
        else:
            for i in num:
                if i == '.':
                    count = indexpoint + 1
                indexpoint += 1
                if i in '0123456789':
                    s3t += i
            if int(num[0]) > 0:
                result = s3t[0]+'.'+s3t[1:]
                print(f'{result} x 10^{count}')
            else:
                result = s3t[0]+'.'+s3t[1:]
                print(f'{result} x 10^{count}')
    else:
        for i in num:
            if i == ' ':
                break
            fill += i
        for i in num:
            if i == '^':
                power = indexpower
            indexpower += 1
        ispower = num[power+1:]
        result = float(fill) * (10**int(ispower))
        print(result)
main(input())
