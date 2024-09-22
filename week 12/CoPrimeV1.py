"""CoPrimeV1"""
def gcd(m,n):
    """gcd"""
    if not n:
        return m
    return gcd(n, m%n)
def main(m, n):
    """main"""
    if gcd(m, n) == 1:
        print('YES')
        print(gcd(m,n))
    else:
        print('NO')
        print(gcd(m,n))
main(int(input()), int(input()))
