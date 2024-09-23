"""Grade III"""
def grade(score):
    """grade"""
    if 95 <= score <= 100:
        return 4
    elif 90 <= score < 95:
        return 3.5
    elif 85 <= score < 90:
        return 3
    elif 80 <= score < 85:
        return 2.5
    elif 75 <= score < 80:
        return 2
    elif 70 <= score < 75:
        return 1.5
    elif 65 <= score < 70:
        return 1
    elif 60 <= score < 65:
        return 0.5
    elif 0 <= score < 60:
        return 0

def main():
    """main"""
    num = int(input())
    allscore = 0
    for _ in range(num):
        allscore += grade(float(input()))
    avg = allscore / num
    print(f"{avg:.2f}")
main()

print()

