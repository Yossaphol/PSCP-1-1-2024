"""area"""
def main(n):
    """main"""
    count = 0
    for _ in range(n):
        col = input().strip()
        col = col.replace(" ", "")
        count += len(col)
    print(count)
main(int(input()))
