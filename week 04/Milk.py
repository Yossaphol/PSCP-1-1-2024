"""Milk"""
def main(a,b,c,d):
    """main"""
    s3t = d // a
    count = 0
    result = 0
    if not b:
        print(s3t)
    else:
        while s3t > 0:
            s3t -= 1
            count += 1
            result += 1
            if count == b:
                result += c
                s3t += 1
    print(int(result))
main(float(input()), int(input()),int(input()),float(input()))
