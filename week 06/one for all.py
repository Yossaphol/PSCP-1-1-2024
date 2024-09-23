"""one for all"""
def main():
    """Main Function"""
    num = int(input())
    result = ''
    for i in range(num):
        name = input()
        if i > 0:
            if not i % 2:
                result += "-" * i
            else:
                result += "*" * i
        result += name
        if i == num -1:
            result += f"_{num}"
    print(result)
main()
