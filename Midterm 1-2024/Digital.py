"""digital"""
def digital(name, nation, house, age, salary, bank):
    """Did you receive digital wallet"""
    con1 = nation in ('Yes', 'True') and house in ('Yes', 'True')
    if con1 and age >= 16 and salary <= 840000 and bank <= 500000:
        print(f'Congratulations! {name} is qualified to receive a digital wallet amount\
 of 10,000 baht, sponsored by all taxpayers in Thailand.')
    else:
        print(f'Unfortunately, {name} is not qualified.')
digital(input(), input(), input(), float(input()), float(input()), float(input()))
