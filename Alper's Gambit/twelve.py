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

def setBalance():
    with open('balList.txt','w') as f:
            f.write(str(user_list)); f.close()

def resultMsg(win):
    if win == True:
        print(f'You won ${bet}! New Balance: {money}')
    elif win == False:
        print(f'You lost ${bet}! New Balance: {money}')
    print(f"Tan's Hand: {tan}")

def giveMoney(donor, taker, donation):
    if user_list[donor][0] >= donation:
        user_list[donor][0] -= donation
        user_list[taker][0] += donation
        print('Money sent successfully!\n')
    else: print("You can't donate more money than you have!\n")
    setBalance()

# LOGIN

try:
    with open('balList.txt','r') as f:
        fileRead = f.read()
        fileRead = fileRead.replace("\'", "\"")
        user_list = json.loads(fileRead)
except: 
    user_list = {}


user = input('Who dis?: ')


# GET BALANCE OF USER / CREATE USER

try:
    print(f'Welcome {user}! You have ${user_list[user][0]}')
except:
    user_list[user] = [500, 0, 0]
    print(f'Welcome {user}! You have ${user_list[user][0]}')

help = f"[COMMANDS]\nq: Quit\nall-in: Bet all your money\nwork: Work and get some money if you don't have any\nstats: View your statistics\ndonate: Donate your money to someone\nhelp: Shows commands\n/////////////////\n"

print(help)

# MENU LOOP

while True:
    money = user_list[user][0]
    total_won = user_list[user][1]
    total_lost = user_list[user][2]
    bet = input(f'You have ${money} How much you want to bet?: ')
    try: bet = int(bet); readyCheck = True
    except: 
        if bet=='q': break
        elif bet=='all-in': bet = money; readyCheck = True
        elif bet=='help': print(help)
        elif bet=='work':
            if money==0:
                user_list[user][0] += ri(0,300)
                setBalance()
            else: print('You still have money. To be able to work, you need to have $0.')
        elif bet=='stats':
            print(f'Current Balance: {money}\nTotal Moneys Won: {total_won}\nTotal Moneys Lost: {total_lost}')
        elif bet=='donate':
            donateTaker = input('\nWrite the name of the person you want to give money to: ')
            donateAmount = int(input('How much money do you want to send?: '))
            try:
                giveMoney(user, donateTaker, donateAmount)
            except:
                print(f"Couldn't found someone named {donateTaker}\n")
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
                total_won += bet
                resultMsg(True)
            if play[0] < play[1]:
                money -= bet
                total_lost += bet
                resultMsg(False)
            if play[0] == play[1]:
                sq_sumE = int(emre[0])**2+int(emre[1])**2
                sq_sumT = int(tan[0])**2+int(tan[1])**2
                if sq_sumE > sq_sumT:
                    money += bet
                    total_won += bet
                    resultMsg(True)
                elif sq_sumE < sq_sumT:
                    money -= bet
                    total_lost += bet
                    resultMsg(False)
                else:
                    print('DRAW')
        if check == 'f':
            money -= int(bet/2)
            total_lost += int(bet/2)
            print(f'Folded. You got your ${bet/2} back')

        user_list[user][0] = money ; user_list[user][1] = total_won ; user_list[user][2] = total_lost
        setBalance()

        emre = []; tan = []; readyCheck = False