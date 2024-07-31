"""SurprisingVote"""
def main(total, highscore):
    """main"""
    if highscore - max(0,total - 2 * highscore) > 2:
        print("Surprising")
    else:
        print("Not surprising")
main(float(input()), float(input()))
