import random
print("="*15+"Dice Game"+"="*15)
player1_n = input("Enter Name Player 1 ") #player1_n ชือ
player2_n = input("Enter Name Player 2 ") #player2_n ชือ
print(f"Welcome {player1_n} & {player2_n} to Dicegame" )
print("="*39)
R = 1
player1_mh = 10 #max hp 1
player2_mh = 10 #max hp 2
def recovery(hp):
    recovery_use=random.randrange(1,10)
    if recovery_use <= 1 and recovery_use:
        print("ร่ายฮิว 1 หน่วย💚")
        return hp+1
    elif recovery_use <= 6 and recovery_use:
        print("ร่ายฮิว 2 หน่วย💚")
        return hp+2
    elif recovery_use == 10 and recovery_use:
        print("ร่ายฮิววืด!! เพราะเค้าลืมคถา")
        return hp+0
    
def skill(hp):
    skill_use=random.randrange(1,10)
    if skill_use <= 5 and skill_use:
        print("โจมตีปกติ DMG-1 🗡️")
        return hp-1
    elif skill_use <= 8 and skill_use:
        print("โจมตีคริติคอล DMG-2 💫")
        return hp-2
    elif skill_use >=9 and skill_use:
        print("ตีวืดดด")
        return hp-0
run = True
while  run:
    for game in range(1):
        player1_v = random.randint(1, 6)
        player2_v = random.randint(1, 6)
        print (f"{player1_n} rolled: {player1_v}")
        print (f"{player2_n} rolled: {player2_v}")
        if player1_v > player2_v:
            print(f"Battel Phese")
            print(f"1 : Attack")
            print(f"2 : Heal")
            player1_c = int(input("Enter List"))
            if player1_c == 1:
                print("="*20)
                print(f"รอบที่ {R} {player1_n} กำลังทำอะไรสักอย่าง")
                player2_mh=skill(player2_mh)                                #โจมตี player 1
                print(player1_n,"ชีวิตเหลือ","❤️"*player1_mh,player1_mh)
                print(player2_n,"ชีวิตเหลือ","❤️"*player2_mh,player2_mh)
                print("="*20)
            elif player1_c ==2:
                print("="*20)
                print(f"รอบที่ {R} {player1_n} กำลังทำอะไรสักอย่าง")
                player1_mh=recovery(player1_mh)                             #ฮิว กันลืม player 1
                print(player1_n,"ชีวิตเหลือ","❤️"*player1_mh,player1_mh)
                print(player2_n,"ชีวิตเหลือ","❤️"*player2_mh,player2_mh)
                print("="*20)
        elif player1_v < player2_v:
            print(f"Battel Phese")
            print(f"1 : Attack")
            print(f"2 : Heal")
            player2_c = int(input("Enter List"))
            if player2_c ==1:
                print("="*20)
                print(f"รอบที่ {R} {player2_n} กำลังทำอะไรสักอย่าง")
                player1_mh=skill(player1_mh)                               #โจมตี player 2
                print(player1_n,"ชีวิตเหลือ","❤️"*player1_mh,player1_mh)
                print(player2_n,"ชีวิตเหลือ","❤️"*player2_mh,player2_mh)
                print("="*20)
            elif player2_c ==2:
                print("="*20)
                print(f"รอบที่ {R} {player2_n} กำลังทำอะไรสักอย่าง")
                player2_mh=recovery(player2_mh)                             #ฮิว กันลืม  player 2
                print(player1_n,"ชีวิตเหลือ","❤️"*player1_mh,player1_mh)
                print(player2_n,"ชีวิตเหลือ","❤️"*player2_mh,player2_mh)
                print("="*20)
        else:
            print("="*20)
            print("รอบที่",R,"ไม่มีอะไรเกิดขึ้น",player1_n,"และ",player2_n,"ยืนมองหน้ากัน")
            print(player1_n,"ชีวิตเหลือ","❤️"*player1_mh,player1_mh)
            print(player2_n,"ชีวิตเหลือ","❤️"*player2_mh,player2_mh)
            print("="*20)
        R +=1
    if player1_mh <= 0:
        break
    if player2_mh <= 0:
        break
    c = input(f"continue Round y/n ")
    if c.lower() =="y":
        continue
    elif c.lower()=="n":
        break
print("จบเกม")