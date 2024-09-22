"""All_Primes"""
def main(num):
    """main"""
    count = 0
    for i in range(1,num+1):
        if not num % i:
            count += 1
main(int(input()))
