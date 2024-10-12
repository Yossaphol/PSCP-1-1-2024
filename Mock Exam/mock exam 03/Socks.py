"""socks"""
def organize_socks(socks):
    '''main'''
    sock_dict = {}
    for sock in socks:
        if sock in sock_dict:
            sock_dict[sock] += 1
        else:
            sock_dict[sock] = 1
    sorted_socks = sorted(sock_dict.keys())
    result = []
    pair_count = 0
    
    for sock in sorted_socks:
        pairs = sock_dict[sock] // 2
        if pairs > 0:
            result.extend([sock * 2] * pairs)
            pair_count += pairs
    if pair_count > 0:
        print(" ".join(result))
    else:
        print("None")
    print(pair_count)
organize_socks(input())

'''
คุณฉงนมีถุงเท้าอยู่ในลิ้นชักที่เรียงไม่เป็นระเบียบ (ตัวอักษรแต่ละตัว แทนถุงเท้าแต่ละข้าง)

เช่นสมมุติว่ามีในลิ้นชักมีถุงเท้าดังนี้
 
RYRBBYRYRYYYBBB

จะพบว่ามีถุงเท้า R อยู่ทั้งหมด 4 ข้าง หรือ 2 คู่
และมีถุงเท้า Y อยู่ทั้งหมด 6 ข้างหรือ 3 คู่
และมีถุงเท้า B อยู่ทั้งหมด 5 ข้าง และจะถือว่ามีแค่ 2 คู่ เพราะอีกข้างที่เหลือจับคู่ไม่ได้
รวมมีทั้งหมด 7 คู่

ให้ทำการจัดเรียงถุงเท้าในลิ้นชักของคุณฉงนให้เป็นระเบียบ โดยเรียงถุงเท้าตามตัวอักษร A ถึง Z
 จากตัวอย่างด้านบนจะเรียงได้ดังนี้

BB BB RR RR YY YY YY

สังเกตว่า ถุงเท้าของ B 1 ข้างที่เหลืออยู่ จะไม่ถูกนำมาจัดเรียงในลิ้นชัก เพราะว่าไม่มีคู่
 

Input Specification
มี 1 บรรทัด เป็นข้อความ String มีตัวอักษร  A-Z ตัวพิมพ์ใหญ่ทั้งหมด จำนวนหลายตัว แต่มีอย่างน้อย 1 ตัวอักษร อักษรแต่ละตัว แทนถุงเท้าแต่ละข้างที่อยู่ลิ้นชัก

Output Specification
มี 2 บรรทัด

บรรทัดแรก เป็นข้อความ String แทนถุงเท้าที่ถูกจัดเป็นคู่ๆ แต่ละคู่เว้นวรรค 1 ช่อง เรียงตามตัวอักษรจาก A ถึง Z ในลิ้นชัก หากไม่มีถุงเท้าที่สามารถเรียงเป็นคู่ได้เลย ให้ตอบว่า None

บรรทัดที่ 2 เป็นจำนวนถุงเท้าที่เรียงอยู่ในลิ้นชัก หน่วยเป็นจำนวนคู่

Input

RYRBBYRYRYYYBBB
Output

BB BB RR RR YY YY YY
7

Input

KJJJKMMM
Output

JJ KK MM
3
'''