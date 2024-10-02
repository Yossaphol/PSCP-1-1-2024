"""Almostmean"""
def main(n):
    """main"""
    allscore = 0
    my_list = []
    for _ in range(n):
        score = input()
        my_list.append(score.split())
    print(my_list)
    for i in range(n):
        allscore += float(my_list[i][1])
    mean = allscore / n
    print(mean)
    
main(int(input()))
