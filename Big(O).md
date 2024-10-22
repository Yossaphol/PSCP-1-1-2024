สรุปการเปรียบเทียบ:
O(1): เวลาคงที่ ไม่ขึ้นกับขนาดอินพุต
O(log n): เพิ่มขึ้นอย่างช้า ๆ โดยแบ่งครึ่งในแต่ละขั้นตอน
O(n): เพิ่มตามขนาดของอินพุต (การวนทุกตัว)
O(n log n): ผสมผสานระหว่างการวนทุกตัวและการแบ่งครึ่ง
O(x^2): เพิ่มขึ้นในรูปแบบกำลังสองของขนาดอินพุต
O(2^x): เพิ่มขึ้นอย่างรวดเร็วในรูปแบบกำลังสอง
O(n!): เพิ่มขึ้นอย่างมหาศาลในรูปแบบแฟคทอเรียล



ข้อที่ 2: O(n!) - Factorial Time Complexity

สำหรับ O(n!) จะใช้การสร้าง Permutations ของรายการเพื่อค้นหาค่ามากที่สุด โดยวิธีนี้จะมีการคำนวณทั้งหมดของความเป็นไปได้

Permutations คือการจัดเรียงลำดับของสมาชิกในกลุ่มหนึ่ง ๆ ในทางคณิตศาสตร์ การจัดเรียงแต่ละลำดับที่แตกต่างกัน
Permutation ของกลุ่มตัวเลข หมายถึงการเรียงลำดับที่แตกต่างกันของสมาชิกในกลุ่มนั้น ๆ
หากมีสมาชิก n ตัว จำนวนการจัดเรียงที่เป็นไปได้ทั้งหมดจะเท่ากับ n! (n factorial)

ถ้าเรามีชุดของตัวเลข {1, 2, 3} จำนวนการจัดเรียงที่เป็นไปได้ทั้งหมดคือ:
(1, 2, 3)
(1, 3, 2)
(2, 1, 3)
(2, 3, 1)
(3, 1, 2)
(3, 2, 1)
ในกรณีนี้ จะมีทั้งหมด 6 permutations ซึ่งคำนวณได้จาก
3! = 3 × 2 × 1 = 6
การใช้ Permutations
การวิเคราะห์ปัญหา: Permutations มักใช้ในปัญหาการวิเคราะห์ที่เกี่ยวข้องกับการเรียงลำดับหรือการเลือก
การสร้างแบบจำลอง: ในการสร้างแบบจำลองทางสถิติและการคาดการณ์
การสุ่ม: การใช้ permutations เพื่อสร้างการสุ่มหรือการจับคู่ที่ไม่ซ้ำกัน
```py
"""Docstring"""
import itertools

def find_max_permutation(arr):
    """DocString"""
    max_value = float('-inf')  # เริ่มต้นด้วยค่าต่ำสุด
    for perm in itertools.permutations(arr):  # สร้าง Permutations ทั้งหมด
        max_value = max(max_value, max(perm))  # ค้นหาค่าที่มากที่สุด
    return max_value

# ตัวอย่างการใช้งาน
numbers = [3, 1, 4, 1, 5]
print(find_max_permutation(numbers))  # Output: 5
```


ข้อที่ 3: O(2^x) - Exponential Time Complexity

ใช้วิธี Recursion ในการตรวจสอบค่าที่มากที่สุดในรายการ
O(2^x) (Exponential Time Complexity)
ความซับซ้อนแบบนี้จะเพิ่มขึ้นเป็นสองเท่าเมื่อขนาดของอินพุต (x) เพิ่มขึ้นหนึ่งหน่วย
พบได้บ่อยในปัญหาที่มีลักษณะ Recursion เช่น การแก้ปัญหาด้วยวิธีแบ่งครึ่งโดยไม่ใช้ Memoization เช่น Fibonacci แบบธรรมดา
ตัวอย่าง: การหาลำดับที่ x ของ Fibonacci แบบการเรียกตัวเองโดยไม่มีการบันทึกผลที่คำนวณแล้ว
```py
"""DocString"""
def find_max(arr):
    """DocString"""
    if len(arr) == 1:  # กรณีฐาน
        return arr[0]
    else:
        max_of_rest = find_max(arr[1:])  # เรียกฟังก์ชันซ้ำ
        return max(arr[0], max_of_rest)

# ตัวอย่างการใช้งาน
numbers = [3, 1, 4, 1, 5]
print(find_max(numbers))  # Output: 5
```


ข้อที่ 4: O(x^2) - Quadratic Time Complexity

ใช้ Nested Loops เพื่อค้นหาค่ามากที่สุด
O(x^2) (Quadratic Time Complexity)
ความซับซ้อนนี้เกิดขึ้นเมื่อจำนวนขั้นตอนการทำงานเติบโตเป็นกำลังสองของขนาดอินพุต (x)
มักพบในปัญหาที่เกี่ยวข้องกับการทำงานกับข้อมูลในรูปแบบตารางหรือการทำ Nested Loop สองชั้น เช่น การเรียงลำดับแบบ Bubble Sort
ตัวอย่าง: การตรวจสอบทุกคู่ในรายการที่มีขนาด x เช่น การหาค่าคู่ที่มีผลบวกเท่ากัน
```py
"""DocString"""
def find_max(arr):
    """DocString"""
    max_value = float('-inf')
    for i in range(len(arr)):  # วนลูปทุกค่าหนึ่งครั้ง
        for j in range(len(arr)):  # วนลูปทุกค่าหนึ่งครั้ง
            if arr[j] > max_value:
                max_value = arr[j] # ควรใส่อะไรดีน้า
    return max_value

# ตัวอย่างการใช้งาน
numbers = [3, 1, 4, 1, 5]
print(find_max(numbers))  # Output: 5
```


ข้อที่ 5: O(n log n) - Linearithmic Time Complexity

ใช้ Sorting ก่อนแล้วค้นหาค่ามากที่สุด
O(n log n) (Linearithmic Time Complexity)
มักพบในอัลกอริทึมที่เกี่ยวข้องกับการแบ่งครึ่ง เช่น Merge Sort, Heap Sort หรือ Quick Sort ในกรณีที่ดีที่สุดและกรณีเฉลี่ย
n log n หมายถึง มีการแบ่งอินพุตซ้ำๆ (log n) และทำการประมวลผลในแต่ละขั้นตอน (n)
ตัวอย่าง: การเรียงลำดับโดยใช้ Merge Sort บนรายการที่มีขนาด n
```py
"""DocString"""
def merge_sort(arr):
    """DocString"""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    """DocString"""
    sorted_arr = []
    while left and right:
        if left[0] < right[0]:
            sorted_arr.append(left.pop(0))
        else:
            sorted_arr.append(right.pop(0))
    sorted_arr.extend(left if left else right)
    return sorted_arr

# ตัวอย่างการใช้งาน
numbers = [3, 1, 4, 1, 5]

# เรียงลำดับก่อน (O(n log n))
sorted_numbers = merge_sort(numbers)

# หาค่าสูงสุดจากลิสต์ที่เรียงแล้ว
max_value = sorted_numbers[-1]  # ค่าในตำแหน่งสุดท้ายคือค่าสูงสุด
print(max_value)  # Output: 5
```


ข้อที่ 6: O(n) - Linear Time Complexity

ค้นหาค่ามากที่สุดโดยการวนลูปผ่านทุกตัว
O(n) (Linear Time Complexity)
อัลกอริทึมที่มีความซับซ้อนนี้จะทำงานในจำนวนขั้นตอนที่แปรผันตามขนาดของอินพุต (n)
ตัวอย่างเช่น การวนลูปเพื่ออ่านหรือประมวลผลทุกตัวในรายการ
เป็นการประมวลผลทุกตัวในลำดับโดยตรงเพียงครั้งเดียว เช่น การหาค่าที่มากที่สุดในรายการขนาด n
```py
"""DocString"""
def find_max_linear(arr):
    """DocString"""
    max_value = arr[0]
    for num in arr:
        if num > max_value:
            max_value = num # น่าจะเริ่มเก็ทหลักการละหล่ะ ลองใส่ดู
    return max_value

# ตัวอย่างการใช้งาน
numbers = [3, 1, 4, 1, 5]
print(find_max_linear(numbers))  # Output: 5
```


ข้อที่ 7: (log n) - Logarithmic Time Complexity

ใช้ Binary Search ในกรณีที่มีการจัดเรียงลำดับ
O(log n) (Logarithmic Time Complexity)
ความซับซ้อนนี้จะเพิ่มขึ้นในลักษณะของการแบ่งครึ่งของข้อมูลในแต่ละขั้นตอน
อัลกอริทึมที่ใช้วิธีการแบ่งครึ่ง เช่น Binary Search เป็นตัวอย่างที่ชัดเจน
ตัวอย่าง: การค้นหาค่าที่กำหนดในรายการที่เรียงลำดับแล้วโดยใช้ Binary Search
```py
"""DocString"""
def find_max_binary_search(arr):
    """DocString"""
    arr.sort()  # เรียงลำดับ
    return arr[-1]  # คืนค่าตัวสุดท้าย

# ตัวอย่างการใช้งาน
numbers = [3, 1, 4, 1, 5]
print(find_max_binary_search(numbers))  # Output: 5
```



ข้อที่ 8: O(1) - Constant Time Complexity

เข้าถึงค่าที่มากที่สุดโดยสมมุติว่าเรารู้ค่าที่มากที่สุดแล้ว
O(1) (Constant Time Complexity)
อัลกอริทึมนี้จะทำงานในเวลาเท่าเดิมเสมอ ไม่ขึ้นอยู่กับขนาดของอินพุต (n)
ตัวอย่าง: การเข้าถึงองค์ประกอบในรายการด้วยดัชนี เช่น array[i]
```py
"""DocString"""
def find_max_constant(arr):
    """DocString"""
    return max(arr)  # คืนค่ามากที่สุดโดยตรง

# ตัวอย่างการใช้งาน
numbers = [3, 1, 4, 1, 5]
print(find_max_constant(numbers))  # Output: 5
```