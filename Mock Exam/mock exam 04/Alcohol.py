"""Alcohol"""
def main(sex, weight, licen, volume, alc):
    """main"""
    amount = int(input())
    hour = int(input())
    if licen == 'Yes':
        drunk = (volume * (alc)) / 100
        past = 15 * hour
        if sex == 'Male':
            drink = (drunk / (weight * 6.8)) * amount
            if (drink*1000) - past >= 50:
                print('Not Safe')
            else:
                print('Safe')
        else:
            drink = (drunk / (weight * 5.5)) * amount
            past = 15 * hour
            if (drink*1000) - past >= 50:
                print('Not Safe')
            else:
                print('Safe')
    else:
        print('Not Safe')
main(input(), float(input()), input(), float(input()), float(input()))
