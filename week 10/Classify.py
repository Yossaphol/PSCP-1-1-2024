"""classify"""
def main():
    """Classify"""
    person = []
    while True:
        tmp = input()
        if tmp.upper() == "END":
            break
        person.append(tmp[:4])
    old = 0
    for i in sorted(set(person)):
        year = int(i[:2])
        print(year if year != old else "--", int(i[2:4]), person.count(i))
        old = year
main()
