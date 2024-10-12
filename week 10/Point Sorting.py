"""Point Sorting"""
def main():
    """Point Sorting"""
    num = int(input())
    listpoint = []
    for _ in range(num):
        numchud = int(input())
        for _ in range(numchud):
            listpoint.append(tuple(map(int, input().split())))
        listpoint.sort(reverse=True, key=lambda x: x[1])
        listpoint.sort(key=lambda x: x[0]+x[1])
        for i in range(numchud):
            print(listpoint[i][0], listpoint[i][1])
        listpoint = []
main()
