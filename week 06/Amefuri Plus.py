"""Amefuri Plus"""
def night(i, wet):
    """night"""
    if i == 'C':
        wet -= 0.25
    elif i == 'N':
        wet -= 0.5
    elif i == 'W':
        wet -= 0.75
    return wet
def noon(i, wet):
    """noon"""
    if i == 'C':
        wet -= 0.5
    elif i == 'N':
        wet -= 1
    elif i == 'W':
        wet -= 1.5
    return wet
def main(h, log):
    """main"""
    wet = 8
    hour = h
    lost = False
    for i in log:
        if wet > 16:
            wet = 16
        if wet <= 0:
            break
        if hour == 25:
            hour = 1
        if i == 'H' and wet > 0:
            lost = True
            break
        if i == 'R':
            wet += 2
        elif i == 'S':
            wet += 3
        if 6 <= hour < 18:
            wet = noon(i, wet)
            hour += 1
        elif 0 <= hour < 6 or 18 <= hour <= 24:
            wet = night(i, wet)
            hour += 1
    if lost is True:
        print('Lost')
    elif not wet:
        print('Dry')
    else:
        print(f"Still Wet (Wet Level: {wet:.2f})")
main(int(input()), input().upper())
