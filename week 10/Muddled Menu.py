"""Muddled Menu"""
def main():
    """Muddled Menu"""
    ans = []
    while True:
        menu = input()
        if menu == "DONE":
            break
        if menu == "CLOSED":
            ans = []
            return print("Full Course: "+str(ans)+" Reversed: "+str(ans))
        elif menu[0:10] == "Can't do: ":
            ans.remove(menu[10:])
        elif menu == "SOMETHING'S WRONG":
            ans.clear()
            continue
        else:
            menu = menu.split(" #")
            if menu[1].isnumeric():
                ans.insert(int(menu[1])-1, menu[0])
            else:
                ans.append(menu[0])
    print("Full Course: "+str(ans)+" Reversed: "+str(ans[::-1]))
main()
