"""d"""
Type = input()
num1 = float(input())
num2 = float(input())
num3 = float(input())
POS1 = 0
POS2 = 0
POS3 = 0
if Type == "Ascend":
    if num1 <= num2 <= num3:
        POS1 = num1
        POS2 = num2
        POS3 = num3
    elif num1 <= num3 <= num2:
        POS1 = num1
        POS2 = num3
        POS3 = num2
    elif num2 <= num1 <= num3:
        POS1 = num2
        POS2 = num1
        POS3 = num3
    elif num2 <= num3 <= num1:
        POS1 = num2
        POS2 = num3
        POS3 = num1
    elif num3 <= num1 <= num2:
        POS1 = num3
        POS2 = num1
        POS3 = num2
    elif num3 <= num2 <= num1:
        POS1 = num3
        POS2 = num2
        POS3 = num1
elif Type == "Descend":
    if num1 >= num2 >= num3:
        POS1 = num1
        POS2 = num2
        POS3 = num3
    elif num1 >= num3 >= num2:
        POS1 = num1
        POS2 = num3
        POS3 = num2
    elif num2 >= num1 >= num3:
        POS1 = num2
        POS2 = num1
        POS3 = num3
    elif num2 >= num3 >= num1:
        POS1 = num2
        POS2 = num3
        POS3 = num1
    elif num3 >= num1 >= num2:
        POS1 = num3
        POS2 = num1
        POS3 = num2
    elif num3 >= num2 >= num1:
        POS1 = num3
        POS2 = num2
        POS3 = num1
print(f'{POS1:.2f}, {POS2:.2f}, {POS3:.2f}')
