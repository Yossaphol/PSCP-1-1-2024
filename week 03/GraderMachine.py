"""GraderMachine"""
def main():
    """main"""
    begin = int(input())
    end = int(input())
    num=0
    num2=''
    if begin <= end:
        for i in range(begin,end+1):
            if not i % 2:
                num += i
                num2 += str(i) + " "
        print(f"pass : {num2}")
        print(f"Sum : {num}")
    else:
        for i in range(end,begin+1):
            if not i % 2:
                num += i
                num2 += " "+str(i)
        print(f"pass : {num2[::-1]}")
        print(f"Sum : {num}")
main()
