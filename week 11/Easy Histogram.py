"""Easy Histogram"""
def main(txt):
    """main"""
    my_dict = {}
    for i in txt:
        if i != ' ':
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1
    sorted_dict = sorted(my_dict.keys(), key=lambda x: (x[0].upper(), x[0].isupper()))
    for i in sorted_dict:
        print(f"{i} = {my_dict[i]}")
main(input())
