import os

def initMenu(verification):
    heading = "Python Checkbook Management"
    mes1 = "1: Please enter the correct password before you can use the other menu items."
    mes1Ver = "1: User Verified \t \t" + "Current Balance: $" + str(balance())
    mes2 = "2: Add, Edit, Void a check"
    mes3 = "3: Add, Edit, Void a deposit"
    mes4 = "4: Reconcile with the Bank"
    mes5 = "5: Exit"
    preMenu = heading + "\n" + "\n" + mes1 + "\n" + mes5
    mainMenu = heading + "\n" + "\n" + "\n" + mes1Ver + "\n" + mes2 + "\n" + mes3 + "\n" + mes4 + "\n" + mes5
    
    if verification == True:
        print(mainMenu)
        userInput = input("")
        userInput = rangeValid(userInput, 1, 5)
        return userInput

    if verification == False:
        print(preMenu)
        userInput = input("")
        return userInput
            
def main():
    cont, passw, choice = True, "", ""
    while cont:
        choice = initMenu(False)
        passw = password(choice)
        if passw:
            while cont:
                choice = initMenu(True)
                if choice == 1:
                    print("\nUser is already verified. \n")
                if choice == 2:
                    cont = checkMenu()
                elif choice == 3:
                    cont = depositMenu()
                elif choice == 4:
                    cont = reconcileMenu()
                elif choice == 5:
                    cont = False
        else:
            if choice == "5":
                cont = False

def balance():
    try:
        balance = open('balance.txt','r')
        line = balance.readline()
        line = format(float(line),'.2f')
        message = line
        balance.close()
        return message
    
    except:
        message = "Your bank account has no record of activity"
        data = open('balance.txt','a')
        data.close()
        return message

def addBal(num):
    balance = open('balance.txt','r')
    temp = open('temp_balance.txt','w')
    bLine = balance.readline()
    if bLine == "":
        bLine = 0
        
    summ = float(bLine) + num
    temp.write(str(summ))

    balance.close()
    os.remove('balance.txt')
    os.rename('temp_balance.txt','balance.txt')

def depositMenu():
    
    cont = True
    bal = 0
    while cont == True:
        print("1: Add a Deposit")
        print("2: Edit a Deposit")
        print("3: Void a Deposit")
        print("4: Back")
        choice = input("")
        choice = rangeValid(choice,1,4)
        if choice == 1: #Write number to file
            cont = depositAdd()
        elif choice == 2:
            cont = depositEdit()
        elif choice == 3:
            cont = depositVoid()
        elif choice == 4:
            cont = False
            
    return True

def depositAdd():
    data = open("deposits.txt","a")
    print("how much is the deposit?")
    depositStr = input("$")
    depositStr = posFloatValid(depositStr, "")
    if depositStr == "quit":
        return True
    depositStr = format(float(depositStr),".2f")
    depositStr = depositStr + "\n"
    data.write(depositStr)
    data.close()
    addBal(float(depositStr))
    return True

def depositEdit():
    
    cont = True
    while cont == True:
        data = open("deposits.txt","r")
        count = 0
        index = 0
        #Display Deposits
        for line in data:
            amount = format(float(line),".2f")
            amount = str(amount)
            count += 1
            row = "Deposit"+str(count)+": "+amount
            print(row)
        print("Type \"back\" to go back")
        #Get new value and confirm
        print("Which deposit would you like to edit?")
        toEdit = input("")
        if toEdit.lower() == "back":
            return True
        toEdit = rangeValid(int(toEdit), 1, count)
        if toEdit == "quit":
            return True
        print("What do you want the new amount to be?")
        newAmt = input("$")
        newAmt = posFloatValid(newAmt, "")
        if newAmt == "quit":
            return True
        print("Deposit number",toEdit,"will now be",str(newAmt),". Is this correct? Y/N")
        ans = input("")
        ans = boolValid(ans,"")
        if ans == True:
            data.close()

            #Edit Checks
            print("temp")
            temp_file = open('temp_file.txt','w')
            data = open('deposits.txt','r')
            line = data.readline()
            while line != "":
                index += 1
                line = line.rstrip('\n')
                if index == int(toEdit):
                    temp_file.write(str(newAmt) + "\n")
                    difference = float(newAmt) - float(line)
                    addBal(difference)
                else:
                    temp_file.write(line + "\n")
                line = data.readline()
            cont = False
        
            data.close()
            temp_file.close()
            os.remove('deposits.txt')
            os.rename('temp_file.txt','deposits.txt')
        else:
            data.close()
    
    return True



def depositVoid():
    
    cont = True
    while cont == True:
        data = open("deposits.txt","r")
        count = 0
        index = 0
        #Display Deposits
        for line in data:
            amount = format(float(line),".2f")
            amount = str(amount)
            count += 1
            row = "Deposit"+str(count)+": "+amount
            print(row)
        print("Type \"back\" to go back")
        #Get new value and confirm
        print("Which deposit would you like to void?")
        toEdit = input("")
        if toEdit.lower() == "back":
            return True
        toEdit = rangeValid(int(toEdit), 1, count)
        if toEdit == "quit":
            return True
        print("Deposit number",toEdit,"will now be voided. Is this correct? Y/N")
        ans = input("")
        ans = boolValid(ans,"")
        if ans == True:
            data.close()

            #Edit Checks
            print("temp")
            temp_file = open('temp_file.txt','w')
            data = open('deposits.txt','r')
            line = data.readline()
            while line != "":
                index += 1
                line = line.rstrip('\n')
                if index != int(toEdit):
                    temp_file.write(line + "\n")
                else:
                    difference = -1 * float(line)
                    addBal(difference)
                line = data.readline()
            cont = False
        
            data.close()
            temp_file.close()
            os.remove('deposits.txt')
            os.rename('temp_file.txt','deposits.txt')
        else:
            data.close()
    
    return True

def checkMenu():
    cont = True
    bal = 0
    while cont == True:
        print("1: Add a Check")
        print("2: Edit a Check")
        print("3: Void a Check")
        print("4: Back")
        choice = input("")
        choice = rangeValid(choice,1,4)
        if choice == 1: #Write number to file
            cont = checkAdd()
        elif choice == 2:
            cont = checkEdit()
        elif choice == 3:
            cont = checkVoid()
        elif choice == 4:
            cont = False
            
    return True

def checkAdd(): #Works
    data = open("data.txt","a")
    print("how much is the check?")
    checkStr = input("$")
    checkStr = checkStr + "\n"
    data.write(checkStr)
    data.close()
    addBal(float(checkStr)*-1)
    return True

def checkVoid():
    
    cont = True
    while cont == True:
        data = open("data.txt","r")
        count = 0
        index = 0
        #Display Checks
        for line in data:
            amount = format(float(line),".2f")
            amount = str(amount)
            count += 1
            row = "Check"+str(count)+": "+amount
            print(row)
        print("Type \"back\" to go back")
        #Get new value and confirm
        print("Which check would you like to void?")
        toEdit = input("")
        if toEdit.lower() == "back":
            return True
        toEdit = rangeValid(int(toEdit), 1, count)
        if toEdit == "quit":
            return True
        
        print("Check number",toEdit,"will now be voided. Is this correct? Y/N")
        ans = input("")
        ans = boolValid(ans,"")
        if ans == True:
            data.close()

            #Edit Checks
            print("temp")
            temp_file = open('temp_file.txt','w')
            data = open('data.txt','r')
            line = data.readline()
            while line != "":
                index += 1
                line = line.rstrip('\n')
                if index != int(toEdit):
                    temp_file.write(line + "\n")
                else:
                    difference = float(line) * 1
                    addBal(difference)
                line = data.readline()
            cont = False
        
            data.close()
            temp_file.close()
            os.remove('data.txt')
            os.rename('temp_file.txt','data.txt')
        else:
            data.close()
    
    return True

def checkEdit():

    cont = True
    while cont == True:
        data = open("data.txt","r")
        count = 0
        index = 0
        #Display Checks
        for line in data:
            amount = format(float(line),".2f")
            amount = str(amount)
            count += 1
            row = "Check"+str(count)+": "+amount
            print(row)
        print("Type \"back\" to go back")
        #Get new value and confirm
        print("Which check would you like to edit?")
        toEdit = input("")
        if toEdit.lower() == "back":
            return True
        toEdit = rangeValid(int(toEdit), 1, count)
        if toEdit == "quit":
            return True
        print("What do you want the new amount to be?")
        newAmt = input("$")
        newAmt = posFloatValid(newAmt, "")
        if newAmt == "quit":
            return True
        print("Check number",toEdit,"will now be",str(newAmt),". Is this correct? Y/N")
        ans = input("")
        ans = boolValid(ans,"")
        if ans == True:
            data.close()

            #Edit Checks
            temp_file = open('temp_file.txt','w')
            data = open('data.txt','r')
            line = data.readline()
            while line != "":
                index += 1
                line = line.rstrip('\n')
                if index == int(toEdit):
                    temp_file.write(str(newAmt) + "\n")
                    difference = float(line) - float(newAmt)
                    addBal(difference)
                else:
                    temp_file.write(line + "\n")
                line = data.readline()
            cont = False
        
            data.close()
            temp_file.close()
            os.remove('data.txt')
            os.rename('temp_file.txt','data.txt')
        else:
            data.close()
    
    return True



def reconcileMenu():
    checkSum = 0
    depositSum = 0
    reconciled = False
    print("What does the bank say your balance is? \nAt any point, type \"back\" to go back")
    bank = input("")
    if bank == "back":
        return True
    bank = floatValid(bank,"")
    if bank == "quit":
        return True
    bal = float(balance())
    diff = bank - bal
    diff = abs(diff)
    print("You and the bank differ by $", str(diff))
    
    print("Do you have any outstanding checks? y/n")
    ans = input("")
    if ans == "back":
        return True
    ans = boolValid(ans,"")
    if ans == "quit":
        return True
    if ans:
        print("How many?")
        ans = input("")
        if ans == "back":
            return True
        ans = posIntValid(ans,"")
        for i in range(ans):
            if i == 0:
                index = "first"
            elif i == 1:
                index = "second"
            elif i == 2:
                index = "third"
            elif i == 3:
                index = "4th"
            elif i > 3 and i%10 != 1 and i%10 !=2 and i%10 !=3:
                index = str(i+1) + "th"
            print("What is the value of the",index,"outstanding check?")
            check = input("")
            if check == "back":
                return True
            check = floatValid(check,"")
            checkSum += check
        print("The total of your outstanding checks is",checkSum)
        bank -= checkSum
        diff = bank - bal
        if diff == 0:
            print("This accounts for the difference. Give the bank some time, they're a little slow sometimes")
            reconciled = True
        else:
            print("You now have a difference of", diff, "to account for")
            print("The Bank's records: $",bank)
            print("Your records: $",bal)

    print("Do you have any outstanding deposits? y/n")
    ans = input("")
    if ans == "back":
        return True
    ans = boolValid(ans,"")
    if ans:
        print("How many?")
        ans = input("")
        if ans == "back":
            return True
        ans = posIntValid(ans,"")
        for i in range(ans):
            if i == 0:
                index = "first"
            elif i == 1:
                index = "second"
            elif i == 2:
                index = "third"
            elif i > 2 and i%10 != 1 and i%10 !=2 and i%10 !=3:
                index = str(i) + "th"
            print("What is the value of the",index,"outstanding deposit?")
            deposit = input("")
            deposit = floatValid(deposit,"")
            depositSum += deposit
        print("The total of your outstanding deposits is $",format(depositSum,'.2f'))
        bank += depositSum
        diff = bank - bal
        if diff == 0:
            print("This accounts for the difference. Give the bank some time, they're a little slow sometimes")
            reconciled = True
        else:
            print("You still have a difference of $", format(diff,'.2f'), "to account for. Sorry Charlie.")
            reconciled = False
    print("Your records: $",bal)
    print("The bank's records: $", bank)
    if reconciled == False:
        print("Would you like to reconcile your records with the bank? y/n")
        ans = input("")
        if ans == "back":
            return True
        ans = boolValid(ans,"")
        if ans:
            print("Are you sure? You can't undo this function. y/n")
            ans = input("")
            ans = boolValid(ans,"")
            if ans:
                addBal(diff)
            else:
                return True
                
    return True

def password(password):
    if password == "asdf":
        return True
    else:
        return False

#boolean input validation

def boolValid(ans, message):
    count = 1
    answer = True
    message = "Use 'Y' or 'N' " + message
    while ans != "Y" and ans != "y" and ans != "N" and ans != "n" and ans != "quit" and count <= 3:
        print(message)
        ans = input("")
        count += 1
    if ans == "Y" or ans == "y":
        answer = True
    elif ans == "N" or ans == "n":
        answer = False
    elif ans == "quit":
        answer = "quit"
    elif count == 4:
        print("You tried too many times, perhaps another look at the menu.")
        answer = "quit"
    return(answer)

#Positive Integer Validation

def posIntValid(value, message):
    count = 1
    correct = False
    message2 = "Please input a positive integer " + message
    message3 = "You have tried 3 extra times, would you like to quit? Y/N"

    while count < 5 and correct == False:
        try:
            value = float(value)
            if value >= 0 and value % 1 == 0:
                correct = True
                return(int(value))
            else:
                if count == 4:
                    print(message3)
                    again = input("")
                    again = boolValid(again, "")
                    if again == False:
                        count = 1
                    else:
                        return("quit")
                else:
                    count += 1
                    value = input(message2)
        except:
            if count == 4:
                print(message3)
                again = input("")
                again = boolValid(again, "")
                if again == False:
                    count = 1
                else:
                    return("quit")
            else:
                count += 1
                value = input(message2)



#Range Integer Validation

def rangeValid(value, low, high):
    count = 1
    correct = False
    message2 = "Please input a positive integer between " + str(low) + " and " + str(high)
    message3 = "You have tried 3 extra times, would you like to go back? Y/N"

    while count < 5 and correct == False:
        try:
            value = float(value)
            if value >= low and value <= high and value % 1 == 0:
                correct = True
                return(value)
            else:
                if count == 4:
                    print(message3)
                    again = input("")
                    again = boolValid(again, "")
                    if again == False:
                        count = 1
                    else:
                        return("quit")
                else:
                    count += 1
                    value = input(message2)
        except:
            if count == 4:
                print(message3)
                again = input("")
                again = boolValid(again, "")
                if again == False:
                    count = 1
                else:
                    return("quit")
            else:
                count += 1
                value = input(message2)

#Positive Float Validation

def posFloatValid(value, message):
    count = 1
    correct = False
    message2 = "Please input a positive number " + message
    message3 = "You have tried 3 extra times, would you like to go back? Y/N"

    while count < 5 and correct == False:
        try:
            value = float(value)
            if value >= 0:
                correct = True
                value = format(value, '.2f')
                return(value)
            else:
                if count == 4:
                    print(message3)
                    again = input("")
                    again = boolValid(again, "")
                    if again == False:
                        count = 1
                    else:
                        return("quit")
                else:
                    count += 1
                    value = input(message2)
        except:
            if count == 4:
                print(message3)
                again = input("")
                again = boolValid(again, "")
                if again == False:
                    count = 1
                else:
                    return("quit")
            else:
                count += 1
                value = input(message2)


def floatValid(value, message):
    count = 1
    correct = False
    message2 = "Please input a positive number " + message
    message3 = "You have tried 3 extra times, would you like to go back? Y/N"

    while count < 5 and correct == False:
        try:
            value = float(value)
            correct = True
            return(value)
        
        except:
            if count == 4:
                print(message3)
                again = input("")
                again = boolValid(again, "")
                if again == False:
                    count = 1
                else:
                    return("quit")
            else:
                count += 1
                value = input(message2)


main()
