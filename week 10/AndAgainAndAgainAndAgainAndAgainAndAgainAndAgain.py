"""AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain"""
def main():
    """AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain"""
    ans = []
    word = input().replace(".", "")
    wordlist = word.split()
    for i in wordlist:
        total = i.count("a") + i.count("e") + i.count("i") + i.count("o") + i.count("u")
        if total >= 2:
            ans.append(i)
    ans.sort()
    if not len(ans):
        print("Nope")
    else:
        for i in ans:
            print(i)
main()
