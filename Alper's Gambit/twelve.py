# Alper 12 sayısının tüm doğal sayı bölenlerinin her birini ayrı ayrı kağıtlara yazarak bir torbaya atıyor. Emre ve Tan bu torbadan
# ikişer tane kağıt çekiyor. Çektikleri kağıtların üzerinde yazan sayıların çarpımı büyük olan oyunu kazanıyor, eğer çarpımları eşit
# ise kareleri toplamı büyük olan oyunu kazanıyor. Emre'nin torbadan çektiği kağıtların üzerinde yazan sayılar 3 ve 4 olduğuna göre
# oyunu Tan'ın kazanması için çekmesi gereken sayıların toplamı aşağıdakilerden hangisi olabilir?

from random import randint as ri
import json

papers = [1,2,3,4,6,12]; emre = []; tan = []; readyCheck = False

# FUNCTIONS

def papersPlease(person=list, t=int):
    while t>0:
        person.append(papers[ri(0,5)])
        t -=1
    return person

def gambit(player,bot):
    deckP = player[0]*player[1]
    deckB = bot[0]*bot[1]
    return deckP,deckB

# LOGIN

try:
    with open('testList.txt','r') as f:
        fileRead = f.read()
        fileRead = fileRead.replace("\'", "\"")
        user_list = json.loads(fileRead)
except: 
    user_list = {}

user = input('Who dis?: ')

# GET BALANCE OF USER / CREATE USER

try:
    print(f'Welcome {user}! You have ${user_list[user]}')
except:
    user_list[user] = 100
    print(f'Welcome {user}! You have ${user_list[user]}')

help = f'[COMMANDS]\nq: Quit\nall-in: Bet all your money\nhelp: Shows commands\n/////////////////\n'

print(help)

# MENU LOOP

while True:
    money = user_list[user]
    bet = input(f'You have ${money} How much you want to bet?: ')
    try: bet = int(bet); readyCheck = True
    except: 
        if bet=='q': break
        elif bet=='all-in': bet = money; readyCheck = True
        elif bet=='help': print(help)
        else: print('Please enter an amount.')
    try: 
        if bet>money:
            print("You can't bet more money than you have.")
        else:pass
    except: pass

    # GAME

    while readyCheck:
        print('YOUR DECK')
        print(papersPlease(emre,2))
        papersPlease(tan,2)
        check = input('Do you want to play or fold? (p/f): ')
        if check == 'p':
            play = gambit(emre,tan)
            if play[0] > play[1]:
                money += bet
                print(f'You won ${bet}! New Balance: {money}')
                print(f"Tan's Hand: {tan}")
            if play[0] < play[1]:
                money -= bet
                print(f'You lost ${bet}! New Balance: {money}')
                print(f"Tan's Hand: {tan}")
            if play[0] == play[1]:
                sq_sumE = int(emre[0])**2+int(emre[1])**2
                sq_sumT = int(tan[0])**2+int(tan[1])**2
                if sq_sumE > sq_sumT:
                    money += bet
                    print(f'You won ${bet}! New Balance: {money}')
                    print(f"Tan's Hand: {tan}")
                if sq_sumE < sq_sumT:
                    money -= bet
                    print(f'You lost ${bet}! New Balance: {money}')
                    print(f"Tan's Hand: {tan}")
        if check == 'f':
            money -= int(bet/2)
            print(f'Folded. You got your ${bet/2} back')

        user_list[user] = money
        with open('testList.txt','w') as f:
            f.write(str(user_list))

        emre = []
        tan = []
        readyCheck = False