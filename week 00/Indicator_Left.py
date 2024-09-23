"""indicator left"""
def main():
    """main"""
    length = int(input())
    line = int(input())
    half = line // 2
    halfafter = half
    while half > 0:
        print(" " * half + "*" * length)
        half -= 1
    print("*" * length)
    after = 1
    while after <= halfafter:
        print(" " * after + "*" * length)
        after += 1
main()
