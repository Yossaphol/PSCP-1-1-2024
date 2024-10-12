"""BreachTheDoor"""
def main():
    """BreachTheDoor"""
    print(*filter(lambda x: len(x) > 6, \
(["".join(j for j in i if j.isalpha()) for i in input().split(" ")])))
main()
