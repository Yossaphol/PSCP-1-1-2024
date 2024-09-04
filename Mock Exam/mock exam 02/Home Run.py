"""Home Run"""
def main(n,distance):
    """main"""
    count = 0
    for _ in range(n):
        feild = float(input())
        if distance > feild:
            count += 1
    print(count)
main(int(input()), float(input()))
