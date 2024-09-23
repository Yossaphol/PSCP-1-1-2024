"""donut"""
def donut(a,b,c,d):
    """DONUT"""
    pay = d * a
    donuts = d
    if c > 0 and (((d//(b+c)))*b)*a <= pay:
        pay = (((d//(b+c)))*b)*a
        donuts = (d//(b+c)) * (b+c)
        if donuts < d and d-donuts < b:
            pay += (d-donuts)*a
            donuts += (d-donuts)
        elif donuts < d and d-donuts >= b:
            donuts += b+c
            pay += b*a
    print(pay,donuts)
donut(int(input()),int(input()),int(input()),int(input()))

# a #price of donut per piece
# b #buy (piece)
# c #get free (piece)
# d #want (piece)