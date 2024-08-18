"""iphone"""
series = input()
storage = input()
if series == "iPhone 13 mini":
    if storage[:3] == '128':
        print(25900)
    elif storage[:3] == '256':
        print(29900)
    elif storage[:3] == '512':
        print(37900)
    else:
        print("Not Available")
elif series == "iPhone 13":
    if storage[:3] == '128':
        print(29900)
    elif storage[:3] == '256':
        print(33900)
    elif storage[:3] == '512':
        print(41900)
    else:
        print("Not Available")
elif series == "iPhone 13 Pro":
    if storage[:3] == '128':
        print(38900)
    elif storage[:3] == '256':
        print(42900)
    elif storage[:3] == '512':
        print(50900)
    elif storage == '1 TB':
        print(58900)
    else:
        print("Not Available")
elif series == "iPhone 13 Pro Max":
    if storage[:3] == '128':
        print(42900)
    elif storage[:3] == '256':
        print(46900)
    elif storage[:3] == '512':
        print(54900)
    elif storage == '1 TB':
        print(62900)
    else:
        print("Not Available")
else:
    print("Not Available")
