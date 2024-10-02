"""LineSorting"""
def main(n):
    """main"""
    list_sort = []
    txt = []
    for _ in range(n):
        text = input()
        txt.append(text)
        list_sort.append(len(text))
    list_sort.sort()
    for i in list_sort:
        for j in txt:
            if len(j) == i:
                print(j)
main(int(input()))
