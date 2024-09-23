"""Elo"""
def main():
    """Main Function"""
    Ra = int(input())
    Rb = int(input())
    ab = input()
    if ab == 'A':
        result = 1 / (1 + 10**((Rb - Ra)/400))
    else:
        result = 1 / (1 + 10**((Ra - Rb)/400))
    print(f"{result:.2f}")
main()
