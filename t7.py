#Author: aviv aloni

import time #For the delay

decorator = []  # Define decorator

def multy(num):
    found = False
    for dict in decorator:
        if dict["input"] == num: #Input found!
            found = True
            return dict["output"]
    if not found:
        time.sleep(3) #For the delay
        x = num*2 #This what the function do
        decorator.append({"input":num, "output":x}) #Add to decorator
        return x

while True:
    x = int(input("Insert a number <0 to exit>: "))
    if x == 0:
        exit()
    else:
        print(str(multy(x)))