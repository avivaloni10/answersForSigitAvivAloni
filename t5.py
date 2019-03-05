#Author: aviv aloni

def check(s): #Check if the ID is israeli or not
    if s.__len__() != 9:
        return False
    else:
        l = []
        sum = 0
        for i in range(0, 7, 2): #calc 2 numbers each iteration
            x1 = int(s[i]) #The first
            x2 = int(s[i + 1]) * 2 #The second
            if x2 >= 10:
                m = x2 % 10
                x2 /= 10
                x2 = int(x2)
                x2 += m
            l.append(x1) #Add first
            l.append(x2) #Add second
        for i in l:
            sum += i
        m = sum % 10
        if sum == sum - m: #If the right digit is 0
            if s[8] == 0: #Check with last digit
                return True
            else:
                return False
        else:
            if (10 - m) == int(s[8]): #Check with last digit
                return True
            else:
                return False

x = input("Insert an israeli ID: ")
print(check(x))