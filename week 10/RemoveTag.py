"""RemoveTag"""
def main():
    """main"""
    word = input().replace("<", "*<").replace(">", ">*").split("*")
    ans = list(filter(lambda x, ok="<": ok not in x, word))
    answer = ' '.join(ans)
    print(answer.split())
main()
