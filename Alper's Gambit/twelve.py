# Alper 12 sayısının tüm doğal sayı bölenlerinin her birini ayrı ayrı kağıtlara yazarak bir torbaya atıyor. Emre ve Tan bu torbadan
# ikişer tane kağıt çekiyor. Çektikleri kağıtların üzerinde yazan sayıların çarpımı büyük olan oyunu kazanıyor, eğer çarpımları eşit
# ise kareleri toplamı büyük olan oyunu kazanıyor. Emre'nin torbadan çektiği kağıtların üzerinde yazan sayılar 3 ve 4 lduğuna göre
# oyunu Tan'ın kazanması için çekmesi gereken sayıların toplamı aşağıdakilerden hangisi olabilir?

from random import randint as ri

papers = [1,2,3,4,6,12]
emre = []
tan = []
readyCheck = False

def papersPlease(person=list, t=int):
    i = 2
    while i>0:
        person.append(papers[ri(0,5)])
        i -=1
    return person

def gambit(player,bot):
    deckP = player[0]*player[1]
    deckB = bot[0]*bot[1]
    return deckP,deckB

def getUser(username):
    try:
        with open("balance.py","r") as f:
            pass
    except:
        with open("balance.py","a") as f:
            f.write(str(user) + " = {'balance' : 100}")

#            f.write(str(user) + " = {'balance' : " + str(money) + "}")

user = input('Who dis?: ')

help = f'[COMMANDS]\nq: Quit\nall-in: Bet all your money\nhelp: Shows commands\n/////////////////\n'

print(help)

while True:
    bal = open("balance.txt", "r+")
    money = int(bal.read())
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

        bal.truncate(0)
        bal.seek(0)
        bal.write(str(money))

        emre = []
        tan = []
        readyCheck = False