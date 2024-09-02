"""Real"""
def circuit1(c0, c1, c2, c3, c4, c5, c6, dp):
    """ICS toa mae"""
    a = c0 == 'on'
    b = c1 == 'on'
    c = c2 == 'on'
    d = c3 == 'on'
    e = c4 == 'on'
    f = c5 == 'on'
    g = c6 == 'on'
    point = dp == 'on'
    pos1 = 11
    dot1 = 0
    if b and c and not a and not d and not e and not f and not g:
        pos1 = 1
    elif not c and not f and a and b and d and e and g:
        pos1 = 2
    elif not e and not f and a and b and c and d and g:
        pos1 = 3
    elif not a and not d and not e and b and c and f and g:
        pos1 = 4
    elif not b and not e and a and c and d and f and g:
        pos1 = 5
    elif not b and a and c and d and e and f and g:
        pos1 = 6
    elif a and b and c and not d and not e and f and not g:
        pos1 = 7
    elif a and b and c and d and e and f and g:
        pos1 = 8
    elif not e and a and b and c and d and f and g:
        pos1 = 9
    elif not g and a and b and c and d and e and f:
        pos1 = 0
    if point :
        dot1 = 1
    return pos1, dot1
def circuit2(c0, c1, c2, c3, c4, c5, c6, dp):
    """ICS toa mae"""
    a = c0 == 'on'
    b = c1 == 'on'
    c = c2 == 'on'
    d = c3 == 'on'
    e = c4 == 'on'
    f = c5 == 'on'
    g = c6 == 'on'
    point = dp == 'on'
    pos2 = 11
    dot2 = 0
    if b and c and not a and not d and not e and not f and not g:
        pos2 = 1
    elif not c and not f and a and b and d and e and g:
        pos2 = 2
    elif not e and not f and a and b and c and d and g:
        pos2 = 3
    elif not a and not d and not e and b and c and f and g:
        pos2 = 4
    elif not b and not e and a and c and d and f and g:
        pos2 = 5
    elif not b and a and c and d and e and f and g:
        pos2 = 6
    elif a and b and c and not d and not e and f and not g:
        pos2 = 7
    elif a and b and c and d and e and f and g:
        pos2 = 8
    elif not e and a and b and c and d and f and g:
        pos2 = 9
    elif not g and a and b and c and d and e and f:
        pos2 = 0
    if point :
        dot2 = 1
    return pos2, dot2
def circuit3(c0, c1, c2, c3, c4, c5, c6, dp):
    """ICS toa mae"""
    a = c0 == 'on'
    b = c1 == 'on'
    c = c2 == 'on'
    d = c3 == 'on'
    e = c4 == 'on'
    f = c5 == 'on'
    g = c6 == 'on'
    point = dp == 'on'
    pos3 = 11
    dot3 = 0
    if b and c and not a and not d and not e and not f and not g:
        pos3 = 1
    elif not c and not f and a and b and d and e and g:
        pos3 = 2
    elif not e and not f and a and b and c and d and g:
        pos3 = 3
    elif not a and not d and not e and b and c and f and g:
        pos3 = 4
    elif not b and not e and a and c and d and f and g:
        pos3 = 5
    elif not b and a and c and d and e and f and g:
        pos3 = 6
    elif a and b and c and not d and not e and f and not g:
        pos3 = 7
    elif a and b and c and d and e and f and g:
        pos3 = 8
    elif not e and a and b and c and d and f and g:
        pos3 = 9
    elif not g and a and b and c and d and e and f:
        pos3 = 0
    if point :
        dot3 = 1
    return pos3, dot3
def main():
    """real of fake"""
    one = circuit1(input(),input(),input(),input(),input(),input(),input(),input())[1]
    two = circuit2(input(),input(),input(),input(),input(),input(),input(),input())[1]
    three = circuit3(input(),input(),input(),input(),input(),input(),input(),input())[1]
    print(one, two, three)
main()
