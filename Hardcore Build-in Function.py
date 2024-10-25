#1 lambda function ในบรรทัดนั้น
double = lambda x : x * 2
print(double(15))



#2 zip คือ การจับคู่ระหว่าง iterable ที่อยู่ในตำแหน่งเดียวกัน
# ต้องใช้ tuple แปลงออกมา
fruit = ('apple', 'banana', 'grape')
color = ('red', 'yellow', 'green', 'purple')

mix = zip(fruit, color)
print(mix)
print(list(mix))



#3 map เป็นการเรียกใช้ function ด้วยการใน iterable แต่ละตำแหน่งมา แล้วนำค่าที่ได้มาเก็บไว้ในตำแหน่งนั้นๆ
#การใช้ ตัวแปร = map(funcitonที่ต้องการใช้, ชื่อตัวแปร iterable ที่ต้องการเรียกใช้)
#ต้องแปลงเป็น list
number = [-5, -7 , -3, -1, -9]
result = map(abs, number)
print(list(result))


#4 ฟังก์ชัน reduce() ใน Python ใช้ในการรวม (reduce) ลิสต์หรือ iterable โดยการใช้ฟังก์ชันที่ทำงานกับสองค่า ซึ่งจะทำการประมวลผลค่าทีละสองค่าจนกว่าจะได้ค่าผลลัพธ์สุดท้าย โดย reduce() เป็นส่วนหนึ่งของโมดูล functools จึงต้องทำการนำเข้าโมดูลก่อนใช้

# ในการใช้งาน อย่าลืม from functools import reduce
from functools import reduce
# สามารถใช้งานได้หลายแบบ เช่น การรวมค่าตัวเลขในลิสต์
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers) # นำ lambda ที่เรียนมา มาใช้ในส่วนของ reduce ได้
print(result) 

words = ["Hello", " ", "World", "!"]

# ใช้ reduce เพื่อรวมสตริง
result = reduce(lambda x, y: x + y, words, "PSCP ") # สามารถใช้ initializer เพื่อกำหนดค่าผลลัพธ์เริ่มต้นได้
print(result)


#ข้อที่ 5: isinstance

#ฟังก์ชัน isinstance() ใน Python ใช้เพื่อตรวจสอบว่าค่าวัตถุ (object) ที่ให้มาเป็นอินสแตนซ์ของคลาสที่ระบุหรือไม่ โดย isinstance() จะคืนค่าเป็น True หากวัตถุเป็นอินสแตนซ์ของคลาสหรือทายาทของคลาสนั้น และคืนค่าเป็น False หากไม่ใช่

var_int = 22
var_float = 22.22
var_string = "Hello"

# เราสามารถใช้ isinstance ในการเช็คได้ว่าค่าวัตถุ (object) ที่ให้มาเป็นอินสแตนซ์ของคลาสที่ระบุหรือไม่

print(isinstance(var_int, int)) # ควรออกเป็น int
print(isinstance(var_float, float)) # ใส่อะไรเพื่อให้ออก True ดี
print(isinstance(var_string, (tuple, str))) # สามารถใส่หลายคลาสในแบบ Tuple ได้



#ข้อที่ 6: filter

#ฟังก์ชัน filter() ใน Python ใช้ในการกรองข้อมูลจากลำดับ (เช่น list, tuple, string, etc.) ตามเงื่อนไขที่กำหนดในฟังก์ชัน โดยฟังก์ชันนี้จะคืนค่าเป็น iterator ที่ประกอบด้วยข้อมูลที่ผ่านเงื่อนไขที่กำหนด
# เราสามารถสร้าง Function ขึ้นมาเพื่อ Filter ข้อมูลได้ เช่น ให้คัดตัวเลขจาก List ให้เหลือแค่เลขที่มีค่ามากกว่า 18

ages = [5, 12, 17, 18, 24, 32]
def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)
print(list(adults))