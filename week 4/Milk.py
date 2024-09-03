"""Milk"""
def main(a,b,c,d):
    """main"""
    s3t = d // a
    bottle = 0
    money = a
    result = 0
    if not b:
        print(s3t)
    else:
        while money < d:
            money += a
            bottle += 1
            result += 1
            if bottle == b:
                bottle = 1
                result += c
    print(int(result))
main(float(input()), int(input()),int(input()),float(input()))
