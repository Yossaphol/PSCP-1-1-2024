"""d"""
a = float(input())
b = float(input())
c = float(input())
A = abs(a**2 + b**2 - c**2)
B = abs(a**2 + c**2 - b**2)
C = abs(b**2 + c**2 - a**2)
if A <= 0.01 or B <= 0.01 or C <= 0.01:
    print("Yes")
else:
    print("No")
