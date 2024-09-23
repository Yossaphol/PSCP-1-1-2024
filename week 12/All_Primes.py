"""All_prime"""
def is_prime(num):
    """check prime"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if not num % i:
            return False
    return True
def count_primes(n):
    """count prime"""
    prime_count = 0
    for i in range(2, n + 1):
        if is_prime(i):
            prime_count += 1
    return prime_count
print(count_primes(int(input())))
