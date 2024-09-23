"""Digitnity"""
def sum_number(num):
    '''sum number'''
    while num >= 10:
        ans = 0
        for i in str(num):
            ans += int(i)
        num = ans
    return num

def main():
    """main"""
    while True:
        number = int(input())
        if not number:
            break
        print(sum_number(number))
main()
