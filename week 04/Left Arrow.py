"""Left Arrow"""
def main():
    """main"""
    star = int(input())
    line = int(input())
    half = line // 2
    i = 0
    j = half
    while j > 0:
        print(" "*j+"*"*star)
        j -= 1
    while i <= half:
        print(" "*i+"*"*star)
        i += 1
main()
