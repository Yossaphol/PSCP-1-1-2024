"""pH"""
def main(ph):
    """main"""
    if ph == 7:
        print('neutral')
    elif 0 <= ph < 7:
        print('acidic')
    elif 7 < ph <= 14:
        print('akaline')
    else:
        print('error')
main(float(input()))
