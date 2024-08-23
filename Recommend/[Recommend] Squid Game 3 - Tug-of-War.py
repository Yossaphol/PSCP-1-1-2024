"""Squid Game 3 - Tug-of-War"""
def main():
    """main"""
    numa = 0
    numb = 0
    for _ in range(10):
        num1 = int(input())
        numa += num1
    for _ in range(10):
        num2 = int(input())
        numb += num2
    if numa < numb:
        print("A")
    elif numa > numb:
        print("B")
    else:
        print("AB")
main()
