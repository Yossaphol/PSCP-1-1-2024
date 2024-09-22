"""GCD_v2"""
def main(m, n):
    """GCD_v"""
    if not n:
        return m
    return main(n, m%n)
print(main(int(input()), int(input())))
