#โครงสร้างควบคุมแบบทำซ้ำ
#range มีหน้าที่กำหนดรอบว่าจะให้ทำงานกี่รอบ โครงสร้างจะมี start,stop,step เริ่มเท่าไหร่จบที่เท่าไหร่
#การเริ่มต้นนับรอบจะเริ่มต้นที่ 0,1,2,3
#การเขียนแบบสามตัวเลือกมี start เริ่มที่เท่าไหร่
#stop จบที่เท่าไหร่ แต่ถ้ากำหนดรอบ6รอบมันจบรอบที่6แต่ค่าตัวแปลที่เก็บได้จะมีแค่5เพราะมันจะหยุดทำงานที่6และออกจากloopไป
#ง่ายๆก็คือค่าที่ได้จาก stop จะ -1
#step เพิ่มที่ละเท่าไหร่

for x in range(1,13) :
    sum=1*x
    print("รอบที่",sum,)