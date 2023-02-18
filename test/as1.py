import random
print("="*15+"Dice Game"+"="*15)
player1_n = input("Enter Name Player 1 ") #player1_n ชือ
player2_n = input("Enter Name Player 2 ") #player2_n ชือ
print(f"Welcome {player1_n} & {player2_n} to Dicegame" )
print("="*39)
player1_mh = 10 #max hp 1
player2_mh = 10 #max hp 2

def skill(hp):
    skill_use=random.randrange(1,10)
    if hp >1 : 
        if skill_use >= 1 and skill_use <=7:
            print("โจมตีปกติ 1 damage")
            return hp-1
        elif skill_use >= 8 and skill_use <=10:
            print("โจมตีคริ 2 damage")
            return hp-2
    else :
        return hp-1
run = True
while  run:
    for game in range(1):
        player1_v = random.randint(1, 6)
        player2_v = random.randint(1, 6)
        print (f"{player1_n} rolled: {player1_v}")
        print (f"{player2_n} rolled: {player2_v}")
        if player1_v > player2_v:
            print("="*20)
            print(f"{player1_n} Win !")
            player2_mh=skill(player2_mh)
            print(f"{player1_n}ชีวิตเหลือ: {player1_mh}")
            print(f"{player2_n}ชีวิตเหลือ:{player2_mh}")
            print("="*20)
        elif player1_v < player2_v:
            print("="*20)
            print(f"{player2_n} Win !")
            player1_mh=skill(player1_mh)
            print(f"{player1_n}ชีวิตเหลือ: {player1_mh}")
            print(f"{player2_n}ชีวิตเหลือ:{player2_mh}")
            print("="*20)
        else:
            print("="*20)
            print("draw")
            print("="*20)
    if player1_mh == 0:
        break
    if player2_mh == 0:
        break
    c = input(f"continue Round y/n ")

    x=str(c).lower()

    print(x)
    if x =="y"  :
        print("continue")
        continue
    if x =="yes"  :
        print("continue")
        continue
    if x=="n" :
        break
    if x=="no" :
        break
    else :
        print("ไปเริ่มเกมใหม่เองนะ")
        break
print("จบเกม")