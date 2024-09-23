"""savecomputerrepeat"""
def main():
    """main"""
    start = 492137954293754252786
    millisec = start
    sec = millisec // 1000
    millisec = millisec % 1000
    mins = sec // 60
    sec = sec % 60
    hour = mins // 60
    mins = mins % 60
    day = hour // 24
    hour = hour % 24
    print(day, hour, mins, sec, millisec)
main()
