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

#Name Validation

def nameValid(string, message):
    count = 1
    correct = False
    message = "We do not accept names with symbols or numeric characters. " + message
    message3 = "You have tried 3 extra times, would you like to quit? Y/N"

    while count <= 4 and correct == False:
        if string.isalpha() == True:
            correct = True
            return(string)
        elif count == 4:
            print(message3)
            again = input("")
            again = boolValid(again, "")
            if again == False:
                count = 1
            else:
                return("quit")
        else:
            count += 1
            string = input(message)


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

#Range Integer Validation

def rangeValid(value, low, high):
    count = 1
    correct = False
    message2 = "Please input a positive integer between " + str(low) + " and " + str(high)
    message3 = "You have tried 3 extra times, would you like to quit? Y/N"

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
    message3 = "You have tried 3 extra times, would you like to quit? Y/N"

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

    
