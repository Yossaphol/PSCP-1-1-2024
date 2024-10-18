"""MissingNumber"""
def main(n):
    """main"""
    my_list = []
    for i in range(1,n+1):
        my_list.append(i)
    while True:
        num = int(input())
        if not num:
            break
        my_list.remove(num)
    for x in my_list:
        print(x)
main(int(input()))
