#data type & Variable
'''
premitive คือ ชนิดข้อมูลพื้นฐาน
integers หรือ int คือแสดงผลตัวเลขจำนวนเต็ม เช่น 1 100 200
Floating point หรือ float คือแสดงผลตัวเลขทศนิยม เช่น0.33 0.111 120.36
string หรือ str คือแสดงผลออกมาเป็นตัวอักษร "hello" "Thongtae"
ฺbooleans หรือ bool คือ แสดงข้อมูลเป็น จริง หรือ เท็จ
'''
'''
non prmitive
Dictionaries หรือ dict
lists หรือ list คือแสดงผลของ odject เป็นแบบโครงสร้าง (10,"hello",20.21)
Tuples หรือ tup
Sets หรือ set
'''
#Variable หรือ ตัวแปล 
#โครงสร้างตัวแปลคือ ชื่อตัวแปล = ค่าที่เก็บในตัวแปล
x = 10 #คือ ชื่อตัวแปล คือ x และ ค่าค่าที่เก็บในตัวแปลคือ 10 เป็นชนิดข้อมูล int
print(x) 
#แต่ถ้าจะต้องแปลง int หรือตัวเลขให้เป็นข้อความก่อน ต้องใชั str(ใส่ข้อมูลที่เป็นint)
#ทำไมถึงต้องแปลงชนิดข้อมูลก่อนเพราะการแสดงผลของ string ไม่สามารถต่อด้วย int ได้จึงต้องแปลง int เป็น str 
print("ผลลัพธ์ = "+str(x))
#้ถ้าจะเช็คว่าตัวแปลหรือข้อมูลของเรานั้นเป็น type อะไรใช้คำสั้ง Print(type(ตัวแปลหรือข้อมูล))
print(type(x))