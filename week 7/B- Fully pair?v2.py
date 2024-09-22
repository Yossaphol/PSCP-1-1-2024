'''B - Fully pair?'''
def pair(alphabet):
    '''main'''
    keep = ""
    none = ""
    count = 0
    for i in alphabet:
        if keep.count(i) <= 0:
            keep += i
    for i in keep:
        if alphabet.count(i) % 2:
            none += i
            count += 1
    if not count:
        print("fully paired")
    else:
        print(none)
pair(input().lower())
