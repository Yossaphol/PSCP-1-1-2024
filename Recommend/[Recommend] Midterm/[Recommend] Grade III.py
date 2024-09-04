"""Grade III"""
import math
def main():
    """main"""
    time = int(input())
    grade = 0
    # allscore = 0
    for _ in range(time):
        num = float(input())
        if 95 <= num <= 100:
            grade += 4
        elif 90 <= num < 95:
            grade += 3.5
        elif 85 <= num < 90:
            grade += 3
        elif 80 <= num < 85:
            grade += 2.5
        elif 75 <= num < 80:
            grade += 2
        elif 70 <= num < 75:
            grade += 1.5
        elif 65 <= num < 70:
            grade += 1
        elif 60 <= num < 65:
            grade += 0.5
        elif 0 <= num < 60:
            grade += 0
    avg = grade / time * 100
    result = math.floor(avg)
    print(f"{result/100:.2f}")
main()
