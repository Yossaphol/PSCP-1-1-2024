"""Taking Turns"""
import json
def main(mylist):
    """main"""
    my_list = json.loads(mylist)
    num = len(my_list)
    i = 0
    j = num - 1
    count = 0
    ind = []
    for z in range(num):
        ind.append(z)
    new = []
    while ind:
        if not count % 2:
            new.append(my_list[i])
            i += 1
            ind.pop(i)
        else:
            new.append(my_list[j])
            j -= 1
            ind.pop(j)
        count += 1
    print(new)
main(input())
