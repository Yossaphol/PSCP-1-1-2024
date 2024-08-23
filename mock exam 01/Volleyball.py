"""result match"""
txt = input()
a = 0
b = 0
seta = 0
setb = 0
count = 0
for i in txt:
    if i == 'A':
        a += 1
    else:
        b += 1
    if seta + setb == 4:
        if a==15 and b <=13 or a > 15 and a == b - 2:
            seta += 1
            count += 1
            a = 0
            b = 0
        if b==15 and a <=13 or b > 15 and b == a - 2:
            setb += 1
            count += 1
            a = 0
            b = 0
    if seta < 3 and setb < 3:
        if a==25 and b <=23 or a > 25 and a == b - 2:
            seta += 1
            count += 1
            a = 0
            b = 0
        if b==25 and a <=23 or b > 25 and b == a - 2:
            setb += 1
            count += 1
            a = 0
            b = 0
for i in range(1,count+2):
    print(f"Set {i}: A ({a}) | B ({b})")

if seta + setb < 5:
    print("The game has not finished yet.")
else:
    if (seta == 3 and not setb) or (seta == 3 and setb == 1) or (seta == 3 and setb == 2):
        print(f"A won {seta}:{setb} set")
    elif (setb == 3 and not seta) or (setb == 3 and seta == 1) or (setb == 3 and seta == 2):
        print(f"B won {setb}:{seta} set")
