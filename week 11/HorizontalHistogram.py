"""HorizontalHistogram"""
def main(txt):
    """main"""
    lower = {}
    upper = {}
    for i in txt:
        if i.isupper():
            if i in upper:
                upper[i] += 1
            else:
                upper[i] = 1
        else:
            if i in lower:
                lower[i] += 1
            else:
                lower[i] = 1
    sort_lower = sorted(lower.keys())
    sort_upper = sorted(upper.keys())
    # Print for lowercase letters with the vertical bar logic
    for i in sort_lower:
        count = lower[i]
        if count > 5:
            print(f"{i} : " + ('-' * 5 + '|') * (count // 5) + '-' * (count % 5))
        else:
            print(f"{i} : {'-'*count}")
    
    # Print for uppercase letters with the vertical bar logic
    for i in sort_upper:
        count = upper[i]
        if count > 5:
            print(f"{i} : " + ('-' * 5 + '|') * (count // 5) + '-' * (count % 5))
        else:
            print(f"{i} : {'-'*count}")
main(input())
