"""Duplicate I"""
def main(n, m):
    """main"""
    list_a = []
    list_b = []
    result = []
    check = n
    if check < m:
        check = m
    for _ in range(n):
        num_a = int(input())
        list_a.append(num_a)
    for _ in range(m):
        num_b = int(input())
        list_b.append(num_b)
    for i in range(check):
        if len(list_a) > len(list_b):
            if list_a[i] in list_b:
                result.append(list_a[i])
        else:
            if list_b[i] in list_a:
                result.append(list_b[i])
    result.sort(reverse=True)
    temp = len(result)
    if not temp:
        print('Nope')
    else:
        for i in result:
            print(i)
main(int(input()), int(input()))
