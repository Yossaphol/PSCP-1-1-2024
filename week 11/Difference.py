"""difference"""
def main(m, n):
    """main"""
    a = set()
    b = set()
    for _ in range(m):
        a.add(int(input()))
    for _ in range(n):
        b.add(int(input()))
    result = sorted(a.difference(b))
    print(*result)
main(int(input()), int(input()))
