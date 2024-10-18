"""WordSequence I"""
def main(txt):
    """main"""
    for i in range(len(txt)):
        print(txt[:i+1])
main(input())
