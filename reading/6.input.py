#function input
#จะใช้คำสั่ง input() มันจะรับค่าที่ผู้ใช้พิมเข้าแล้วนำไปเก็บไว้ในตั้วแปล
#เช่น name = input("ชื่อผู้ใช่งาน : ") ข้อความในวงเล็บจะไม่นับว่าเป็นข้อความที่ป้อนเขามาแต่จะรับแต่สิ่งที่พึ่งพิมเข้ามา
#แต่ข้อมูลที่รับมาจะเป็น str ทั้งหมด
'''
name = input("ชื่อผู้ใช้ : ")
print("user include :",name)
'''
#แล้วถ้าจะรับตัวเลขให้การเป็น int เลย
#แบบที่แปลงข้อมูลก่อนแล้วค่อยเก็บค่า
'''
ืีnumber1 = int(input("กรุณาระบุหมายเลขที่1 =")) 
number2 = int(input("กรุณาระบุหมายเลขที่2 ="))
print(number1+number2)
'''
#แบบยังไม่แปลงค่าแล้วเก็บใส่ตัวแปล
'''
ืีnumber1 = input("กรุณาระบุหมายเลขที่1 =")
number2 = input("กรุณาระบุหมายเลขที่2 =")
print(int(number1)+int(number2))
'''
#ในกรณีนี้เราไม่จำเป็นต้องแปลงค่า str เป็น int หลังจากเก็บค่าเข้าตัวแปลแล้ว แต่จะแปลงค่าตั้งแต่รับinputแล้วเก็บใส่ตัวแปลเลย
#แต่มันก็แล้วแต่ว่าเราจะเอาข้อมูลไปใช้แบบไหน