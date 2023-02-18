#โปรแกรมคำนวร BMI(ดัชนีมวลกาย)
#BMI = น้ำหนัก(kg)/ส่วนสูง**2(m)

weight=int(input("น้ำหนักของท่าน (kg) = "))
hight=int(input("ส่วนสูงของท่าน (cm) = "))/100
BMI=weight/(hight**2)
print("BMI ของท่าน : ",BMI)
normalBMI=(18.5<=BMI<=22.9)
print("BMI ของท่านเกินเกณฑ์ปกติ :",not normalBMI)
