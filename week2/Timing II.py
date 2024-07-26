"""timing II"""
def main():
    """main"""
    sec = int(input())
    day = sec // 86400 #60*60*24
    sec2 = sec % 86400
    hour = sec2 // 3600
    sec2 = sec % 3600
    mins = sec2 // 60
    sec2 = sec % 60
    if day > 9999:
        print("ERR_:__:__:__")
    else:
        print(f"{day:>04}:{hour:>02}:{mins:>02}:{sec2:>02}")
main()
