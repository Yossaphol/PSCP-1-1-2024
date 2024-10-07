"""[ Challenge ] (หมู) เห็ด (เป็ด) ไก่"""
def main(all_leg, all_head):
    """main"""
    # leg = 2x + 4y
    # head = x + y
    for x in range(all_head+1):
        y = all_head - x
        if (2*x) + (4*y) == all_leg:
            print(x)
            print(y)
main(int(input()),int(input()))
