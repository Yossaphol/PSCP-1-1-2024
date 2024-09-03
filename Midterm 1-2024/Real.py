# จงหาค่าของตัวเลขที่แสดงผลบน 7-Segment display ของ 3 ตัวนี้

#Input Specification
#มี 24 บรรทัด เป็นค่า

#8 บรรทัดแรก เป็นค่า a b c d e f g และ dp ของ 7 segment LED ตัวที่ 1 ตัวซ้ายสุด ตามลำดับ
#8 บรรทัดต่อมา เป็นค่า a, b, c, d, e, f, g และ dp ของ 7 segment LED ตัวที่ 1 ตัวกลาง ตามลำดับ
#8 บรรทัดสุดท้าย เป็นค่า a, b, c, d, e, f, g และ dp ของ 7 segment LED ตัวที่ 1 ตัวขวาสุด ตามลำดับ

#แต่ละบรรทัดมีค่าเป็น on หรือ off เท่านั้น

#Output Specification
#1 บรรทัดเป็นจำนวนจริงที่มีทศนิยม 2 หลัก
#หากมีทศนิยมไม่ครบ 2 หลัก หรือเป็นจำนวนเต็ม ให้เติมเลข ทศนิยม 0 ให้ครบ
#หากอ่านค่า 7-Segment display ทั้ง 3 ตัวแล้วไม่สามารถแสดงผลเป็นตัวเลข 1 จำนวนได้ หรือ มี 7-Segment #ตัวใดตัวหนึ่งไม่แสดงผลเป็นตัวเลข 0-9 ให้ตอบ Error

# Sample Testcases
# Input
# off
# on
# on
# off
# off
# off
# off
# off
# on
# on
# on
# on
# on
# on
# off
# on
# on
# off
# on
# on
# off
# on
# on
# off
# Expected Output
# 10.50

# Sample Testcases
# Input
# on
# on
# on
# on
# off
# on
# on
# off
# off
# on
# on
# off
# off
# off
# off
# off
# off
# on
# on
# off
# off
# off
# off
# off
# Expected Output

# Sample Testcases
# Input
# off
# on
# on
# off
# off
# off
# off
# off
# on
# on
# off
# on
# on
# off
# on
# off
# on
# on
# on
# on
# off
# off
# on
# on
# Expected Output


# Sample Testcases
# Input
# off
# off
# on
# on
# on
# off
# on
# off
# off
# off
# on
# on
# on
# off
# on
# off
# on
# on
# off
# off
# on
# on
# on
# off
# Expected Output

