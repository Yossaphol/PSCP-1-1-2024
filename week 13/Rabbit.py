"""Rabbit"""
def main(rabbit, jump, carrot):
    """main"""
    for i in range(1,rabbit+1):
        left = (i * (i+1)) / 2
    eaten = (rabbit * (rabbit + 1)) / 2
    jump_left = jump - eaten
    rl = carrot - rabbit
    print
main(int(input()), int(input()), int(input()))
