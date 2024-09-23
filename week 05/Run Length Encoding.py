"""Run Length Encoding"""
def main():
    """main"""
    txt = input()
    check = txt[0]
    result = ''
    sum_ = 0
    for i in txt:
        if i == check:
            sum_ += 1
        else:
            result = result + str(sum_) + check
            check = i
            sum_ = 1
    result = result + str(sum_) + check
    print(result)
main()
