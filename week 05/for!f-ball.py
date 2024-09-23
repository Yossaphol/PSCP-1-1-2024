"""FOR!F-Ball"""
def main():
    """main"""
    txt = input()
    left = 1
    middle = 0
    right = 0
    for i in txt:
        if i == 'A':
            templeft = left
            tempmid = middle
            middle = templeft
            left = tempmid
        elif i == 'B':
            tempmid = middle
            tempright = right
            right = tempmid
            middle = tempright
        else:
            tempright = right
            templeft = left
            left = tempright
            right = templeft
    if left == 1:
        print(1)
    elif middle == 1:
        print(2)
    else:
        print(3)
main()
