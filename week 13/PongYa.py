"""PongYa"""
def main(num):
    """main"""
    if num[-1] == '3' or not int(num) % 3:
        print('PONG')
    else:
        print(num)
main(input())
