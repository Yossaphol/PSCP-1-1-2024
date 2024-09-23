"""Counting Star"""
def main():
    """Main Function"""
    star = str(input())
    constellation = 0
    comet = 0
    shooting_star = 0
    ite = 0
    while ite < len(star) - 1:
        if star[ite] == "~":
            if star[ite + 1] == "*":
                comet += 1
                ite += 2
                continue
        if star[ite] == "*":
            if star[ite + 1] == "~":
                comet += 1
                ite += 2
                continue
            elif star[ite + 1] == "/":
                shooting_star += 1
                ite += 2
                continue
            elif star[ite + 1] == "*":
                constellation += 1
                ite += 2
                continue
        ite += 1
    if constellation >= 1 or comet >= 1 or shooting_star >= 1:
        print(f"constellation: {constellation}")
        print(f"comet: {comet}")
        print(f"shooting star: {shooting_star}")
    else:
        print("Tonight is a quiet night.")
main()
