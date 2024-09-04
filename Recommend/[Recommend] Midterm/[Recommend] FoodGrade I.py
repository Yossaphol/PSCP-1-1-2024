'''DOC'''
def check_kai(num,c):
    '''DOC'''
    TC = c
    i = int(input())
    if 50 <= i <= 70:
        TC += 1
    if num-1 <= 0:
        print(TC)
        return
    check_kai(num-1,TC)
check_kai(24,0)