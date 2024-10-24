"""PrasomSib"""
def main(num):
    """main"""
    lst = []
    count = 0
    for i in num:
        lst.append(i)
    length = len(lst)
    i = 0
    a = 0
    result = 0
    while i != length - 1:
        result += int(lst[a])
        if result == 10:
            count += 1
            i += 1
            result = 0
            a = i
            continue
        if a > length:
            break
        a += 1
    print(count)
main(input())
