"""[ Day 1 ] Volume of The Pyramid"""
def main(base, height):
    """main"""
    print(f'{(1/3)*(base**2)*(height):.6f}')
main(float(input()), float(input()))
