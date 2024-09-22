def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes(n):
    prime_count = 0
    for i in range(2, n + 1):
        if is_prime(i):
            prime_count += 1
    return prime_count

# รับค่าจากผู้ใช้
n = int(input("Enter a number: "))
print(count_primes(n))
