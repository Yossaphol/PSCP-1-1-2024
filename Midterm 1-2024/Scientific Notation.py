# Scientific Notation หรือ ตัวเลขสัญกรณ์วิทยาศาสตร์ คือ การเขียนตัวเลขอยู่ในรูปการคูณของเลขยกกำลังที่มีฐานเป็นสิบและเลขชี้กำลังเป็นจำนวนเต็ม มีรูปทั่วไปเป็น a x 10^b เมื่อ 1 ≤ |a| <10 และ b เป็นจำนวนเต็ม ซึ่งมีหลักการในการแปลงดังรูปด้านล่าง


# อธิบายตัวอย่างที่ 1 123000000 -> 1.23 x 10^8 ตัด 0 ทิ้ง เพราะ ตามกฎข้อที่ 5 จะนำเลข 0 ออก ถ้าตอนแรกเลข 0 นั้นอยู่ทางซ้ายของจุดทศนิยม (แต่กรณีนี้ไม่มีจุด ก็ตัดทิ้งเหมือนกัน)
# อธิบายตัวอย่างที่ 3 4590.000 -> 4.590000 x 10^3 ถ้าเลข 0 อยู่ทางขวาของจุดทศนิยมไม่ต้องตัดทิ้ง
# ยกเว้นกรณีของ ตัวอย่างที่ 4 จะไม่มีสัญกรณ์ทางวิทยาศาสตร์สำหรับศูนย์ในรูปแบบ a x 10^b เมื่อ 1 ≤ |a| <10
# จึงให้ตอบเพียงแค่ 0
# จงตรวจสอบว่าข้อมูล Input ที่ได้รับนั้น เป็นตัวเลขที่อยู่ในรูปแบบปกติหรือตัวเลขสัญกรณ์วิทยาศาสตร์
# หากเป็นตัวเลขปกติก็ให้แสดงผลลัพธ์ออกมาในรูปแบบเลขเลขสัญกรณ์วิทยาศาสตร์
# แต่ถ้าหาก Input ที่ได้รับเป็นตัวเลขสัญกรณ์วิทยาศาสตร์อยู่แล้ว ก็ให้แสดงผลออกมาเป็นตัวเลขรูปแบบปกติ
# Input Specification
# 1 บรรทัด

# ตัวเลขจำนวนจริง หรือ ตัวเลขสัญกรณ์วิทยาศาสตร์
# Output Specification
# 1 บรรทัด

# ตามเงื่อนไขของโจทย์ ตัวเลขจำนวนจริง หรือ ตัวเลขสัญกรณ์วิทยาศาสตร์