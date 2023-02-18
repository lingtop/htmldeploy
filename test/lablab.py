print("====BMI====")
height = float(input("input height(centimeter): "))
weight = float(input("input weight(KG): "))
Mheight = height/100
bmi = weight/Mheight**2
if bmi < 18.5:
    print(f"BMI: {bmi:.2f} อยู่ในเกณฑ์ น้ำหนักน้อย")
elif bmi >= 18.5 and bmi < 22.99:
    print(f"BMI: {bmi:.2f} อยู่ในเกณฑ์ ปกติ")
elif bmi >= 23 and bmi < 24.99:
    print(f"BMI: {bmi:.2f} อยู่ในเกณฑ์ ท้วม")
elif bmi >= 25 and bmi < 29.99:
    print(f"BMI: {bmi:.2f} อยู่ในเกณฑ์ อ้วน")
else:
    print(f"BMI: {bmi:.2f} อยู่ในเกณฑ์ อ้วนมาก")