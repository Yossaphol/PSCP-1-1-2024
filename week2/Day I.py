"""leap year"""
cs = int(input())
if not cs % 4:
    if not cs % 100:
        if not cs % 400:
            print("Yes")
        else:
            print("No")
    else:
        print("Yes")
else:
    print("No")
