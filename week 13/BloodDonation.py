"""BloodDonation"""
def main(age, weight, times):
    """main"""
    if (age == 17 or 60 <= age <= 70) and weight >= 45:
        sign = input()
        if sign == 'True' and times:
            print('Yes')
        else:
            print('No')
    elif (18 <= age <= 59) and weight >= 45:
        if age >= 56 and not times:
            print('No')
        else:
            print('Yes')
    else:
        print('No')
main(int(input()), int(input()), int(input()))
