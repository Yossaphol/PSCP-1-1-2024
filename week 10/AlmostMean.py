"""Almostmean"""
def main(n):
    """main"""
    info = []
    score_total = 0
    new = []
    for i in range(n):
        info.append(input().split())
        score_total += float(info[i][1])
    avg = score_total / n
    for j in info:
        gap = avg - float(j[1])
        if gap >= 0:
            new.append(j)
    l = sorted(new,key = lambda x:float(x[1]))
    print(f"{l[-1][0]}\t{l[-1][1]}")
main(int(input()))
