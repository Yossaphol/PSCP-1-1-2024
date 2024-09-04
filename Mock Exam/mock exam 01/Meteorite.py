"""Meteorite"""
def meteorite():
    """main"""
    kilogram = float(input())
    broken = int(input())
    lesskilogram = float(input())
    count = 1
    times = 0
    check = True
    if lesskilogram == kilogram:
        print(1)
    elif lesskilogram > kilogram:
        print(0)
    else:
        while check:
            permeteo = kilogram / broken
            if permeteo <= lesskilogram:
                print(count)
                check = False
            else:
                times += 1
                count += broken ** times
                kilogram = permeteo
meteorite()
