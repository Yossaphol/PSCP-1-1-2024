"""SumOfNumber"""
def main():
    """main"""
    num2 = 0
    num = 0
    tnum = int(input())
    while True:
        num = int(input())
        if num == -1:
            break
        num2 += num
        if num2 == tnum:
            break
    print(num2)
main()
