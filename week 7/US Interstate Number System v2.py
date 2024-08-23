"""US Interstate Number System"""
def road(num):
    """main"""
    count = 0
    if num in ('5', '05', '005'):
        print('Vertical Major Interstate')
        print('I-5')
    elif (len(num) == 2 and num == '00') or (len(num) == 3 and num[1:] == '00'):
        print('Others')
    elif len(num) == 2:
        if num[-1] == '0':
            print("Horizontal Major Interstate")
            print(f"I-{num}")
            count = 1
        elif num[-1] == '5':
            print("Vertical Major Interstate")
            print(f"I-{num}")
            count = 1
        else:
            print('Others')
    elif len(num) == 3 and num[0] != '0':
        if count == 1:
            interstate = 'Odd Minor Interstate'
            if not int(num[0]) % 2:
                interstate = 'Even Minor Interstate'
            print(interstate)
            if num[1:] == '05':
                print('I-5')
            else:
                print(f"I-{num[1:]}")
        else:
            print('Others')
    else:
        print('Others')
road(input())
