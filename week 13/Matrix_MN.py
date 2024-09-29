"""Matrix_MN"""
def main(m, n):
    """main"""
    my_list = []
    for _ in range(m*n):
        i = int(input())
        my_list.append(i)
    for _ in range(m):
        for _ in range(n):
            print(my_list[0],end=' ')
            my_list.pop(0)
        print()
main(int(input()), int(input()))
