"""quadrant"""
def main():
    """main"""
    num1 = int(input())
    num2 = int(input())
    if num1 > 0 and num2 > 0:
        print("Q1")
    elif num1 < 0 < num2:
        print("Q2")
    elif num1 < 0 and num2 < 0:
        print("Q3")
    elif num2 < 0 < num1:
        print("Q4")
    elif not num1 and not num2:
        print("O")
    elif not num1:
        print("Y")
    elif not num2:
        print("X")
main()
