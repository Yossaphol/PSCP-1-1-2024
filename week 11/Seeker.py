"""IAM503ROT8OOSS001LKFD010LLASD123"""
def main(txt):
    """main"""
    new = ''
    result = 0
    for i in txt:
        if i.isnumeric():
            new += i
        else:
            new += ' '
    my_list = new.split()
    for i in my_list:
        result += int(i)
    print(result)
main(input())
