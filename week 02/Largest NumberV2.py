"""largest  number"""
NUM1 = input()
NUM2 = input()
NUM3 = input()
s1 = int(NUM1+NUM2+NUM3)
s2 = int(NUM1+NUM3+NUM2)
s3 = int(NUM2+NUM1+NUM3)
s4 = int(NUM2+NUM3+NUM1)
s5 = int(NUM3+NUM1+NUM2)
s6 = int(NUM3+NUM2+NUM1)
if s1 >= s2 and s1 >= s3 and s1 >= s4 and s1 >= s5 and s1 >= s6:
    print(s1)
elif s2 >= s1 and s2 >= s3 and s2 >= s4 and s2 >= s5 and s2 >= s6:
    print(s2)
elif s3 >= s1 and s3 >= s2 and s3 >= s4 and s3 >= s5 and s3 >= s6:
    print(s3)
elif s4 >= s1 and s4 >= s2 and s4 >= s3 and s4 >= s5 and s4 >= s6:
    print(s4)
elif s5 >= s1 and s5 >= s2 and s5 >= s3 and s5 >= s4 and s5 >= s6:
    print(s5)
elif s6 >= s1 and s6 >= s2 and s6 >= s3 and s6 >= s4 and s6 >= s5:
    print(s6)
