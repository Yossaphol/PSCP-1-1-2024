"""US Interstate Number System"""
def minor(check, num):
    """minor"""
    if check:
        if int(num[0]) % 2:
            print('Odd Minor Interstate')
        else:
            print('Even Minor Interstate')
    else:
        print('Others')
def road(num):
    """main"""
    check = False
    if num in ('5', '05', '005'):
        print('Vertical Major Interstate')
        print('I-5')
    elif (len(num) == 2 and num == '00') or (len(num) == 3 and num[1:] == '00'):
        print('Others')
    elif len(num) == 2:
        if num[-1] == '0':
            print("Horizontal Major Interstate")
            print(f"I-{num}")
        elif num[-1] == '5':
            print("Vertical Major Interstate")
            print(f"I-{num}")
        else:
            print('Others')
    elif len(num) == 3:
        if num[-1] == '0' or num[-1] == '5':
            check = True
        minor(check, num)
        if check:
            if num[1:] == '05':
                print('I-5')
            else:
                print(f"I-{num[1:]}")
    else:
        print('Others')
road(input())
