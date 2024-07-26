"""BootSequence"""
def main():
    """main"""
    num = int(input())
    num2 = ""
    for i in range(1,num):
        num2 += str(i)+"_"
    num2 += str(num)
    print(num2)
main()
