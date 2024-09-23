"""CompositeFunction"""
def f(x):
    """fx"""
    return 2 * x
def g(x):
    """gx"""
    return (x/2)+1
num = int(input())
print(f"{f(g(num)):.2f}")
print(f"{g(f(num)):.2f}")
