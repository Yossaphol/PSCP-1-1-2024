"""RockPaperScissor"""
def main():
    """main"""
    txt = input()
    txt1 = len(txt)
    ascore = 0
    bscore = 0
    dictja = {
        "RP" : "B",
        "RR" : "DRAW",
        "RS" : "A",
        "SS" : "DRAW",
        "SR" : "B",
        "SP" : "A",
        "PP" : "DRAW",
        "PR" : "A",
        "PS" : "B"
    }
    for i in range(0,txt1,2):
        result = dictja[txt[i:i+2]]
        if result == 'A':
            ascore += 1
        elif result == 'B':
            bscore += 1
    if ascore > bscore:
        print('A win',(str(ascore)+'-'+str(bscore)))
    elif bscore > ascore:
        print('B win',(str(bscore)+'-'+str(ascore)))
    else:
        print('DRAW',str(ascore))
main()
