"""isprime_small"""
def is_prime(num):
    """prime number"""
    count = 0
    for i in range(1,num+1):
        if not num % i:
            count += 1
    return count
def main(num):
    """main"""
    result = is_prime(num)
    if result == 2:
        print('Yes')
    else:
        print('No')
main(int(input()))
