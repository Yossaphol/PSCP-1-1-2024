"""Cat parade"""
def main():
    """main"""
    lis = []
    check = []
    while True:
        meow = input()
        if meow == 'END':
            break
        if meow == "IT'S A DOG":
            lis.pop()
            continue
        if meow.find(','):
            lis.extend(meow.split(', '))
        else:
            lis.append(meow)
    sortlist = sorted(lis, key=str.lower)
    for i in sortlist:
        if i not in check:
            print(f"{i} {lis.index(i)+1} {lis.count(i)}")
        check.append(i)
main()
