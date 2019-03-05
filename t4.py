#Author: aviv aloni

def shrinker(s): #Shrinking the strinkg
    new = ""
    counter = 0
    ch = " "
    for c in s:
        if c == ch:
            counter += 1 #Count how many from the char
        else:
            ch = c
            if not counter == 0:
                new += str(counter)
            counter = 1
            new += c
    if not counter == 0:
        new += str(counter)
    return new

s = input("Insert a string: ")
print(shrinker(s))