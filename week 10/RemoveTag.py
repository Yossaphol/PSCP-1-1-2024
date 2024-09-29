"""RemoveTag"""
def main(txt):
    """main"""
    result = []
    storage = ''
    for i in txt:
        if i == '>':
            if i == '<':
                continue
            result += i
        if i == '<':
            result.append(storage[1:].split())
    print(result)
main(input())
