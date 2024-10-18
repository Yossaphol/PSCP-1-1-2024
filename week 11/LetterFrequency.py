"""Letterfrequency"""
def main(txt):
    """main"""
    txt = txt.lower().replace(" ", "")
    my_dict = {}
    for i in txt:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    sort_dict = sorted(my_dict, key=lambda x: my_dict[x], reverse=True)
    print(sort_dict[0])
main(input())
