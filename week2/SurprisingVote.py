"""SurprisingVote"""
def main(total, highscore):
    """main"""
    left = total - highscore
    if highscore - abs(total - 2 * highscore) > 2:
        print("Surprising")
    else:
        print("Not surprising")
main(float(input()), float(input()))
