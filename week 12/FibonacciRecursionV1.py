"""FibonacciRecursionV1"""
def main(n):
    """main"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return main(n-1) + main(n-2)
print(main(int(input())))
