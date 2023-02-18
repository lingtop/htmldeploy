#ตัวดำเนินการตรรกศาตร์
#การวิเคราะห์ทางตรรก ให้ใช้การเปรียบเทียบที่มีผลลัพเป็น Ture กับ False หรือ 1 กับ 0
#AND=และ คือถ้ามีอย่างใดอย่างนึงเป็นเท็จจะได้ false แต่ถ้าเป็นจริงทั้งสองฝั่งจะได้ ture
#OR=หรือ คือถ้าค่าใดค่าหนึ่งเป็นจริงจะเป็น ture แต่ถ้าผิดทั้ง 2 ค่า จะเป็น false
#NOT=ไม่ คือ คั่วตรงข้ามระหว่างจริงกับเท็จ ถ้าคำตอบเป็นจริงจะได้เท็จและถ้าคำตอบเป็นเท็จจะได้จริง

#ตั้งค่า booleans
x = (5<10) #ค่า x เก็บค่า booleans เปรียบเทียบว่า 5น้อยกว่า 10 เป็นจริง
y = (10==5)

#ใช้ AND
print(x and y) # x คือ (5<10) เป็นจริง แต่ y คือ (10==5) เป็นเท็จทำค่าที่ออกมันเป็นเท็จ
#ใช้ or
print(x or y) # เพราะมีค่าใดค่านึงถูกค่าที่ได้ถึงได้ ture
#ใช้ not
print("xมากกว่า10จริงหรือไม่",not x)# เพื่อ 5น้อยกว่า 10 จริงคำตอบที่ได้จึงเป็น false