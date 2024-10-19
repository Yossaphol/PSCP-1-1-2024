"""Stuttering"""
def main(txt):
    """main"""
    my_list = txt.split()
    my_list.append(' ')
    check = True
    lenght = len(my_list)
    i = 0
    while check:
        if my_list[i] == ' ':
            break
        if i < lenght:
            if my_list[i+1] == my_list[i]:
                my_list.pop(i+1)
                lenght -= 1
            else:
                i += 1
        else:
            check = False
    mystring = ' '.join(my_list)
    print(mystring)
main(input())
