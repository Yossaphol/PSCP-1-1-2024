"""Largest Number"""
def main():
    """main"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    pos1 = 0
    pos2 = 0
    pos3 = 0
    if num1 >= num2 >= num3:
        pos1 = num1
        pos2 = num2
        pos3 = num3
    elif num1 >= num3 >= num2:
        pos1 = num1
        pos2 = num3
        pos3 = num2
    elif num2 >= num1 >= num3:
        pos1 = num2
        pos2 = num1
        pos3 = num3
    elif num2 >= num3 >= num1:
        pos1 = num2
        pos2 = num3
        pos3 = num1
    elif num3 >= num1 >= num2:
        pos1 = num3
        pos2 = num1
        pos3 = num2
    elif num3 >= num2 >= num1:
        pos1 = num3
        pos2 = num2
        pos3 = num1
    print(str(pos1)+str(pos2)+str(pos3))
main()
