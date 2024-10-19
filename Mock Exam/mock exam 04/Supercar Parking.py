"""Supercar Parking"""
def main(txt):
    """main"""
    new = txt.replace('01', ' ').replace('10', ' ').replace('1', ' ').strip()
    count = new.count('0')
    print(count//2 + count%2)
main(input())
