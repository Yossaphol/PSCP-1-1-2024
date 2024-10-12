"""Cat Parade"""
def main():
    """Cat Parade"""
    cats = []
    my_list = []
    while True:
        word = input()
        if word == "END":
            break
        if word != "IT'S A DOG":
            for cat in word.split(","):
                cats.append(cat.strip())
                if not my_list.count(cat.strip()):
                    my_list.append(cat.strip())
        elif word == "IT'S A DOG":
            cats.pop()
            my_list.pop()

    my_list.sort()
    for cat in my_list:
        print(cat, cats.index(cat) + 1, cats.count(cat))
main()
