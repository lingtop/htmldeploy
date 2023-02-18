#ternary operator การลดการเขียน if ให้สั่่นลง หรือการลดรูป
#โครงสร้าง
#"เงื่อนไขเป็นจริง" if expression else "เงือนไขอื่นๆ"
'''
age=int(input("กรุณาป้อนอายุ : "))
if age>=15:
    print("วันรุ่น")
else :
    print("วัยเด็ก")
print("END")
'''
#การเขียนแบบลดรูป
age=int(input("กรุณาป้อนอายุ : "))
print("วัยรุ่น") if age>=15 else print("วัยเด็ก")
print("END")
