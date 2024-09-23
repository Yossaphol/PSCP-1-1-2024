"""Counting Stars"""
def main():
    """Counting Stars"""
    stras = input()
    i = 0
    constellation = 0
    comet = 0
    shooting_star = 0
    while i < len(stras)-1:
        type_stras = stras[i]+stras[i+1]
        if type_stras in ('~*', '*~') :
            comet += 1
            i += 2
        elif type_stras == "*/" :
            shooting_star += 1
            i += 2
        elif type_stras == "**" :
            constellation += 1
            i += 2
        else :
            i += 1
    if not constellation and not comet and not shooting_star :
        print("Tonight is a quiet night.")
    else :
        print(f"constellation: {constellation}")
        print(f"comet: {comet}")
        print(f"shooting star: {shooting_star}")
main()
