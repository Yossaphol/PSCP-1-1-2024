"""Alcohol"""
def main(sex, weight, license, volume, alc, amount, hour):
    """main"""
    if license == 'Yes':
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
main(input(), float(input()), input(), float(input()), float(input()), int(input()), int(input()))
