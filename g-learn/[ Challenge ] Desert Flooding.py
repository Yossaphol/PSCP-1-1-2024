"""[ Challenge ] Desert Flooding"""
def main(s, x, y):
    """main"""
    d = ((0-x)**2 + (0-y)**2)**0.5
    count = 0
    s3m = 0
    while s3m < d:
        s3m += s
        count += 1
    print(count)
main(int(input()), int(input()), int(input()))
