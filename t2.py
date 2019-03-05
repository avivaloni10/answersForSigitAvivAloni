#Author: aviv aloni

def showMenu(): #Print the menu
    print("1. Insert list one after one\n2. Insert the complete list\n")
    x = int(input("Insert your choice: "))
    while not (1 <= x and x <= 2):
        print("Wrong input!\nEnter your choice: ")
        x = input()
    return x

def getListOneByOne(): #Get the list one by one
    l = []
    while True:
        x = input("Insert next <insert stop when you done.>: ") #Running until stop
        if x == "stop":
            break
        else:
            l.append(int(x))
    return l

def getCompleteList(): #Get the complete list
    l = []
    x = input("Insert complete list <for example 1,2,3,4>: ")
    numbers = x.split(",") #Split the list of numbers
    for i in numbers:
        l.append(int(i))
    return l

def sumList(l): #Sum of the list
    sum = 0
    for i in l:
        sum += i
    return sum

x = showMenu()
if x == 1:
    l = getListOneByOne()
else:
    l = getCompleteList()
print(str(sumList(l)))