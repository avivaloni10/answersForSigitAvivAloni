#Author: aviv aloni

def print_menu(): #Print the menu
    print("1. Print balance\n2. Get money\n3. Change secret code\n4. exit\n")
    x = int(input("Insert your choice: "))
    while not(1 <= x and x <= 4):
        print("Wrong input!\nEnter your choice: ")
        x = input()
    return x

def getBalance(accounts, code): #Get the balance
    find = False
    for account in accounts:
        if account["code"] == code: #Find the account
            print(str(account["balance"]) + "\n")
            find = True
            break
    if not find:
        print("Account not found.\n")

def getMoney(accounts, code): #Get the money
    x = printGetMoneyMenu()
    if x == 1:
        for account in accounts:
            if account["code"] == code: #Find the account
                account["balance"] -= 20
    elif x == 2:
        for account in accounts:
            if account["code"] == code: #Find the account
                account["balance"] -= 50
    elif x == 3:
        money = int(input("Insert how many money you need: "))
        for account in accounts:
            if account["code"] == code: #Find the account
                account["balance"] -= money
def printGetMoneyMenu(): #Print the "get the money" menu
    print("1. Get 20\n2. Get 50\n3. Get another\n")
    x = int(input("Insert your choice: "))
    while not (1 <= x and x <= 3):
        print("Wrong input!\nEnter your choice: ")
        x = input()
    return x

def changeSecretCode(accounts, code): #Changing secret code
    for account in accounts:
        if account["code"] == code: #Find the account
            otherCode = int(input("Insert new code: "))
            if codeNotFound(accounts, otherCode): #Make sure the code is not in accounts
                account["code"] = otherCode
                print("Done.\n")
            else:
                print("This code is already exist!\n")
            break
def codeNotFound(accounts, code): #Make sure the code is not in accounts
    ret = True
    for account in accounts:
        if account["code"] == code: #Find the account
            ret = False
            break
    return ret;

def run(accounts):
    x = print_menu()
    if x == 4: #If x == 4 there is no need to get the code from user
        exit()
    code = int(input("Insert code: "))
    if x == 1:
        getBalance(accounts, code)
    elif x == 2:
        getMoney(accounts, code)
    elif x == 3:
        changeSecretCode(accounts, code)

accounts = [
    {"code":123456, "balance":20000},
    {"code":456789, "balance":50000},
    {"code":789123, "balance":100000},
] #Define accounts
while True: #Running until exit(x == 4)
    run(accounts)