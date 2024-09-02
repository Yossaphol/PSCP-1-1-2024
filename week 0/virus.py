"""virus"""
def main():
    """main"""
    dna = ''
    while True:
        num = input()
        if num == 'NULL':
            break
        dna += num
    i = 0
    dna_want = ['10101','10001','01010']
    count = [0,0,0]
    while i < len(dna) - 5:
        look = dna[i:i+5]
        if look in dna_want:
            index = dna_want.index(look)
            count[index] += 1
            i += 5
        else :
            i += 1
    print(count)
    print(count[0])
    print(count[1])
    print(count[2])
main()
