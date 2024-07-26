"""howlong"""
def main():
    """main"""
    n = input()
    t = 0
    for idx, i in enumerate(n):
        if not idx and i == '-':
            continue
        t += 1
    print(t)
main()
