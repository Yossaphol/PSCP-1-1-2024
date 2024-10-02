"""[ Day 1 ] Portal"""
def main(x, y, z):
    """main"""
    print(f'({int(x/8)}, {y}, {int(z/8)})')
    print(f'{x//8},{y},{z//8}')
main(int(input()), int(input()), int(input()))
