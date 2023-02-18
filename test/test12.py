input1=input("item : ")
price1=input("price : ")
input2=input("item : ")
price2=input("price : ")
input3=input("item : ")
price3=input("price : ")

if price1 > price2 and price1 > price3 :
    print("สิ่งที่แพงที่สุดคือ",input1,"ราคา ",price1)
elif price2 > price1 and price2 > price3 :
    print("สิ่งที่แพงที่สุดคือ",input2,"ราคา ",price2)
elif price3 > price1 and price3 > price2 :
    print("สิ่งที่แพงที่สุดคือ",input3,"ราคา ",price3)

if price1 < price2 and price1 < price3 :
    print("สิ่งที่ถูกที่สุดคือ",input1,"ราคา ",price1)
elif price2 < price1 and price2 < price3 :
    print("สิ่งที่ถูกที่สุดคือ",input1,"ราคา ",price1)
elif price3 < price1 and price3 < price2 :
    print("สิ่งที่ถูกที่สุดคือ",input1,"ราคา ",price1)