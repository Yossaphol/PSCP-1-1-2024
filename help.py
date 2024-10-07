"""Heads and Legs"""
def main(head, leg):
    """main"""
    if leg < head * 2 or leg % 2 or leg > head * 4:
        print('Impossible')
    else:
        for bird in range(head+1):
            rabbit = head - bird
            if (2 * bird) + (4 * rabbit) == leg:
                print(rabbit, bird)
                break
        # print("---------------")
        # rabbit = leg // 4 if math.ceil(leg / head) >= 4 else 0
        # bird = (leg - (rabbit * 4)) // 2
        # print(rabbit, bird)
main(int(input()), int(input()))
