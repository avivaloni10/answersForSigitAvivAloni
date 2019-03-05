#Author: aviv aloni

def getCompleteList(): #Get the complete list
    l = []
    x = input("Insert complete list <for example 1,2,3,4>: ")
    numbers = x.split(",") #Split the list of numbers
    for i in numbers:
        l.append(int(i))
    return l

def multy(num):
    num *= 2
    return num

def my_map(my_function, my_list):
    result = []
    for i in my_list:
        result.append(my_function(i))
    return result

l = my_map(multy, getCompleteList())
for i in l:
    print(str(i))