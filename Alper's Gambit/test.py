
import json

def readJson():
    with open("balance.json","r") as f:
        balance_list = json.loads(f)
        return type(balance_list)

while True:
    menu = input('what u wanna do babe?: ')
    match menu:
        case '1':
            username = input('username: ')
            x = {'username' : username, 'balance' : 0}
            json_str = username + ' = ' + json.dumps(x) + '\n'
            with open("balance.py","a") as f:
                f.write(json_str)