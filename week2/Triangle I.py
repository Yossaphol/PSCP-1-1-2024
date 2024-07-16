"""d"""
a = float(input())
b = float(input())
c = float(input())
if a**2 == b**2 + c**2:
    print("Yes")
elif b**2 == a**2 + c**2:
    print("Yes")
elif c**2 == a**2 + b**2:
    print("Yes")
else:
    print("No")
