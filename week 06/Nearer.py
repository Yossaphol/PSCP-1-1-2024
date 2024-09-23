"""near"""
def main():
    """main"""
    alice = int(input())
    bob = int(input())
    itim = int(input())
    if abs(itim - alice) == abs(itim - bob):
        print(f"Sundaes {abs(itim - alice)}")
    elif abs(itim - bob) > abs(itim - alice):
        print(f"Alice {abs(itim - alice)}")
    else:
        print(f"Bob {abs(itim - bob)}")
main()
