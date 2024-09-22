"""GCD_v1"""
def main(m, n):
    """GCD_v1"""
    if not n:
        return m
    return main(n, m%n)
print(main(int(input()), int(input())))
