setA = {1,3,4,5}
setB = {1,2,3}

for i in setA:
    print(i)


#ADD
setB.add(7)
print(setB)
#REMOVE ถ้าไม่มีข้อมูลจะขึ้นค่า error
setB.remove(7)
print(setB)
"""setB.remove(9)
print(setB)"""
#UPDATE
x = {1,2,3,4,5,6}
y = {7,8,9}
x.update(y)
print(x)
print(y)
#DISCARD
x.discard(5)
print(x)
#ไม่เหมือนกับ remove ถ้าไม่มีก็จะไม่ได้ลบอะไรออกไป
x.discard(10)
print(x)
#POP ลบตัวหน้า
d = x.pop()
print(x)
print(d)



A = {'red', 'green', 'blue'}
B = {'yellow', 'red' ,'orange'}
#union
print(A | B) #or
print(A.union(B))

#intersection
print(A & B)
print(A.intersection(B))

#difference
print(A - B)
print(A.difference(B))

#symmetric_difference
print(A ^ B)
print(A.symmetric_difference(B))

#issubset
print(A.issubset(B))