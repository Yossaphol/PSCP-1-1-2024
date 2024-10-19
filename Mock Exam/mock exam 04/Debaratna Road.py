"""Debaratna Road"""
def main(km):
    """main"""
    if 0 <= km <= 5.032:
        print('Bangkok')
    elif 5.032 < km <= 35.477:
        print('Samut Prakarn')
    elif 35.477 < km <= 52.9:
        print('Chachoengsao')
    elif 52.9 < km <= 58.855:
        print('Chon Buri')
    else:
        print('InValid')
main(float(input()))
