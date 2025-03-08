"""best before"""
def main(n):
    """main"""
    pos1 = []
    pos2 = []
    countpos1 = 0
    countpos2 = 0
    for _ in range(n):
        date = input()
        pos1.append(date[:2])
        pos2.append(date[2:4])
    for i in pos1:
        if int(i) > 12:
            countpos1 += 1
    for j in pos2:
        if int(j) > 12:
            countpos2 += 1
    if countpos1 >= 1 and not countpos2:
        print('mmddyy')
    elif countpos2 >= 1 and not countpos1:
        print('ddmmyy')
    else:
        print('no clue')
main(int(input()))
