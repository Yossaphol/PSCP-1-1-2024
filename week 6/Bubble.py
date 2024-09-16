"""[Recommend] Bubble"""
def main():
    """main"""
    txt = input()
    jump = 1
    i = 1
    check = txt.find('|')
    goal = 'po'
    im = True
    while i < check and im:
        if txt[i] == ' ':
            goal = 'im'
            im = False
        if txt[i] == 'o':
            jump += 1
            i += 1
        if txt[i] == 'O':
            jump += 1
            i += 3
    if goal == 'im':
        print('IMPOSSIBLE')
        print(len(txt[i:]))
    else:
        print('POSSIBLE')
        print(jump)
main()
