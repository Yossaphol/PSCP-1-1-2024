"""3n"""
def main():
    """main"""
    count = 0
    while True:
        num = int(input())
        if not num:
            break
        while num != 1:
            if not num % 2:
                num = num / 2
            else:
                num = num * 3 + 1
            count += 1
        print(count + 1)
        count = 0
main()
