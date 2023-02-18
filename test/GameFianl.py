import random
import time

player_name = []
player_life = []

print("="*15+"ศึกลูกเต๋าเขย่าโลก"+"="*15)
player_name.append(input("ใส่ชื่อผู้เล่นที่ 1 :")) # player_name[0] ชือ
player_name.append(input("ใส่ชื่อผู้เล่นที่ 2 :")) # player_name[1] ชือ
time.sleep(2)
print(f"ยินดีต้อนรับ {player_name[0]} & {player_name[1]}" )
print("="*39)

time.sleep(3)
print(f"กำลังเข้าสู่การต่อสู่")
# player_life[0] & player_life[1] Max HP
player_life.append(10)
player_life.append(10)

# Dice Point
player1_v = 0           #player value จำนวนแต้มลูกเต๋า
player2_v = 0           #player value จำนวนแต้มลูกเต๋า

round = 1

def recovery(hp):
    print(f"กำลังสุ่มการรักษา")
    time.sleep(3)
    if hp < 10 :
        recovery_use = random.randrange(1, 10)
        if recovery_use <= 1 and recovery_use:
            print("ร่ายฮีล 2 หน่วย💚")
            return hp+2
        elif recovery_use <= 6 and recovery_use:
            print("ร่ายฮีล 4 หน่วย💚")
            return hp+4
        elif recovery_use == 10 and recovery_use:
            print("ร่ายฮีลวืด เพราะเค้าลืมคถา!!")
            return hp+0
    else :              #เลือดจะถูก limit ที่ 12 หน่วยเท่านั้นถ้ามีการฮิวเพิ่ม เลือดจะไม่เพิ่ม
         print("เลือดของคุณเต็ม")
         return hp+0

def skill(hp):
    print(f"กำลังสุ่มทักษะ")
    time.sleep(3)
    skill_use = random.randrange(1, 10)
    if skill_use <= 5 and skill_use:
        print("โจมตีปกติ HP-3 🗡️")
        return hp-3
    elif skill_use <= 8 and skill_use:
        print("โจมตีคริติคอล HP-5 💫")
        return hp-5
    elif skill_use >= 9 and skill_use:
        print("ตีวืดดด เพราะพื้นมันลื่น!!")
        return hp-0

def mainact(name,player):
    while True:
        try:
            print(f"รอบที่ {round} ถึงเวลาการต่อสู้ ของ {name}")
            print(f"1 : โจมตี🗡️")
            print(f"2 : รักษา💚")
            player_c = int(input('ใส่ตัวเลือกด้านบน(1,2): '))
            if player_c ==1 or player_c==2:
               break
            else:
                print("="*16,"Error","="*16)
                print("ใส่อะไรของมึงเนี่ย เอาแค่ 1-2 พอ")
                print("="*39)
        except:
            print("="*16,"Error","="*16)
            print("ใส่อะไรของมึงเนี่ย เอาแค่ 1-2 พอ")
            print("="*39)
        
    print("="*39)
    print(f"รอบที่ {round} {name} กำลังทำอะไรสักอย่าง")
    
    if player == 1: # player1
        if player_c == 1:
            player_life[1] = skill(player_life[1])  # โจมตี player
        elif player_c ==2:
            player_life[0] = recovery(player_life[0])  # ฮีล player
    else: # player2
        if player_c == 1:
            player_life[0] = skill(player_life[0])  # โจมตี player
        elif player_c ==2:
            player_life[1] = recovery(player_life[1])  # ฮีล player
            
    print(player_name[0], "ชีวิตเหลือ", "💚"*player_life[0],player_life[0])
    print(player_name[1], "ชีวิตเหลือ", "💚"*player_life[1], player_life[1])
    print("="*39)
        
while True:
    time.sleep(2)
    while True:
        print(f"กำลังสุ่มทอยลูกเต๋า")
        time.sleep(2)
        player1_v = random.randint(1, 6)
        player2_v = random.randint(1, 6)
        print (f"{player_name[0]} ทอยได้: {player1_v}")
        print (f"{player_name[1]} ทอยได้: {player2_v}")
        
        if player1_v > player2_v:
            mainact(player_name[0],1)
        elif player2_v > player1_v:
            mainact(player_name[1],2)
        else:
            print("="*39)
            print("รอบที่", round, "ไม่มีอะไรเกิดขึ้น",player_name[0], "และ", player_name[1], "ยืนมองหน้ากัน")
            print(player_name[0],"ชีวิตเหลือ","💚"*player_life[0],player_life[0])
            print(player_name[1], "ชีวิตเหลือ","💚"*player_life[1], player_life[1])
            print("="*39)
        
       
        if player_life[0] <= 0  :
            print(f"{player_name[0]} แพ้ ")
            break
        elif player_life[1] <= 0  :
            print(f"{player_name[1]} แพ้ ")
            break
        

        round += 1
        
    con = input(f"ต้องการล้างแค้นไหม จะเอา!!! กด Y :")
    if con.lower() == "y":
        player_life[0] = 10
        player_life[1] = 10
        round = 0
        continue
    else:
        break
    
print("จบเกม")