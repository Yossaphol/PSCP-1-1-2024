"""Sequence N"""
def main():
    '''Variable'''
    N = int(input())
    for i in range(N):
        for j in range(N):
            if not j  or i == j or j == N-1:
                print("*",end="")
            else:
                print(" ",end="")
        print()
main()
