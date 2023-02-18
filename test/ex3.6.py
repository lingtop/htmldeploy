text =input("input :")
def chktext(t):
    i = 0
    chk = "aeiouAEIOU" #สร้างตัวแปรสระขึ้นมา
    for x in range(len(t)): #นับจำนวนข้อความใน t และเปลี่ยนเป็นจำนวนรอบ
        if t[x-1] in chk : #t[x-1]คื่อ index ข้อความเอามาเทียบกับ ตัวแปร chk
            i += 1
    return i
print(chktext(text))