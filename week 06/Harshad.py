"""Harshad"""
def main():
    """main"""
    for _ in range(10):
        number = input()
        num = abs(int(number))
        divide = 0
        for i in str(num):
            divide += int(i)
        if num == '0' or not divide:
            print('No')
        else:
            if not int(num) % int(divide):
                print('Yes')
            else:
                print('No')
main()
