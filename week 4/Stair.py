"""Stair"""
def main():
    """main"""
    tallest = int(input())
    n = int(input())
    height = 0
    count = 0
    for _ in range(n):
        stair = int(input())
        if stair > tallest:
            height = -1
        else:
            height += stair
            if height >= tallest:
                count += 1
                height = stair
    if height >= 0:
        print(count)
    else:
        print("NO")
main()
