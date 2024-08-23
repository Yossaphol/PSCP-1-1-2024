"""US Interstate Number System"""
def road(number):
    """find number of the road"""
    if len(number) == 1 and number == '5':
        print("Vertical Major Interstate")
        print("I-5")
    elif len(number) == 2 and number[-1] in ('0', '5'):
        if number[-1] == '0' and 1 <= int(number[0]) <= 9:
            print("Horizontal Major Interstate")
            print(f"I-{number}")
        elif number[-1] == '5' and 1 <= int(number[0]) <= 9:
            print("Vertical Major Interstate")
            print(f"I-{number}")
        else:
            print("Others")
    elif len(number) == 3 and number[0] != '0':
        if number[1:] == '00':
            print('Others')
        else:
            if not int(number[0]) % 2:
                print("Even Minor Interstate")
            else:
                print("Odd Minor Interstate")
            if number[1] == '0':
                print(f'I-{number[2]}')
            else:
                print(f"I-{number[1:]}")
    else:
        print("Others")
road(input())


#ขาดกรณีที่เป็น 444 ถนนหลักไม่มี 44(num[1,2]) เลยทำให้output เป็นน others