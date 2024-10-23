score = {'Jame': 49, 'Thomas': 52, 'Danny':54, 'Bobby': 56}
number = {1:'one', 2:'two',3:'three', 4:'four'}

print(score['Jame'])
#update item
#var[keys] = values
score['Janny'] = 35
print(score)

#keys ส่่งคืนมาเป็น tuple
print(score.keys())
#values ส่งคืนมาเป็น tuple 
print(score.values())
#items ส่วคืนมาเป็น tuple
print(score.items())
print(list(score.items()))
#get ส่งค่า values ของตัว keys ที่ใส่เข้าไป
print(number.get(1))
#update
number.update({5:'five', 6:'six'})
print(number)
#pop
x = number.pop(4)
print(x)
print(number)
#popitem
a = number.popitem()
print(a)
print(number)


for k, v in score.items():
    print(k,v)

for k in score.keys():
    print(k)

for v in score.values():
    print(v)