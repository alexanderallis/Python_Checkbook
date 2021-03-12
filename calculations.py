import inValid5

breakPoint = 25

#GLOBAL VARIABLES
costYoungZero = 325
costYoungOne = 380
costYoungTwo = 405
costYoungThree = 450
costYoungFourUp = 480

costZero = 275
costOne = 315
costTwo = 365
costThree = 390
costFourUp = 410

#Calculations

def getCost(age, vio):
    global breakPoint
    cost = 0
    if age < breakPoint:
        cost = youngPriceRate(vio)
    else:
        cost = priceRate(vio)
    return(cost)

def youngPriceRate(violations):
    cost = 0
    if violations == 0:
        cost = costYoungZero
    elif violations == 1:
        cost = costYoungOne
    elif violations == 2:
        cost = costYoungTwo
    elif violations == 3:
        cost = costYoungThree
    else:
        cost = costYoungFourUp
    return(cost)

def priceRate(violations):
    cost = 0
    if violations == 0:
        cost = costZero
    elif violations == 1:
        cost = costOne
    elif violations == 2:
        cost = costTwo
    elif violations == 3:
        cost = costThree
    else:
        cost = costFourUp
    return(cost)

def getCalculations(age, violations):
    return(getCost(age, violations))

#Admin Menu

def adminMeta(status):
    while status == "0":
        status = adminMenu(status)
    return("0")

def adminMenu(answer):
    if answer == "0":
        print("Which figures would you like to change?")
        print("1: The breakpoint age")
        print("2: The rates for young drivers")
        print("3: The rates for normal drivers")
        print("4: Go Back")
        answer = input("")
        answer = inValid5.rangeValid(answer, 1, 4)
    else:
        return("quit")

    if answer == 1:
        return(changeBreakpoint())
    elif answer == 2:
        return(changeYoungRates("0"))
    elif answer == 3:
        return(changeRates("0"))
    elif answer == 4:
        return("quit")
        print("return 0")
    else:
        return("quit")

def changeBreakpoint():
    global breakPoint
    correct = False
    while correct == False:
        print("What would you like the break point to be?")
        print("Type \'back\' to go back")
        newBreak = str.lower(input(""))
        if newBreak == "back":
            return("0")
        else:
            newBreak = inValid5.rangeValid(newBreak, 16, 105)
            message = "You want to change the break point to " + str(format(newBreak, '.0f')) + " years old. Is this correct?"
            correct = input(message)
            correct = inValid5.boolValid(correct, "")
    breakPoint = newBreak
    print("The breakpoint is now", str(format(newBreak, '.0f')), "years old.")
    return("0")

def changeYoungRates(ans):

    while ans == "0":
        if ans == "0":
            print("which price bracket would you like to change?")
            print("0: Zero Violations")
            print("1: One Violations")
            print("2: Two Violations")
            print("3: Three Violations")
            print("4: Four or More Violations")
            print("5: Go Back")
            ans = input("")
            ans = inValid5.rangeValid(ans, 0, 5)
            
            if ans == 0:
                ans = (changeCost("youngzero"))
            elif ans == 1:
                ans = (changeCost("youngone"))
            elif ans == 2:
                ans = (changeCost("youngtwo"))
            elif ans == 3:
                ans = (changeCost("youngthree"))
            elif ans == 4:
                ans = (changeCost("youngfour"))
            elif ans == 5:
                return("0")
    return("quit")

def changeRates(ans):

    while ans == "0":
        if ans == "0":
            print("which price bracket would you like to change?")
            print("0: Zero Violations")
            print("1: One Violations")
            print("2: Two Violations")
            print("3: Three Violations")
            print("4: Four or More Violations")
            print("5: Go Back")
            ans = input("")
            ans = inValid5.rangeValid(ans, 0, 5)
            
            if ans == 0:
                ans = (changeCost("zero"))
            elif ans == 1:
                ans = (changeCost("one"))
            elif ans == 2:
                ans = (changeCost("two"))
            elif ans == 3:
                ans = (changeCost("three"))
            elif ans == 4:
                ans = (changeCost("four"))
            elif ans == 5:
                return("0")
    return("quit")

def changeCost(bracket):
    global costYoungZero
    global costYoungOne 
    global costYoungTwo 
    global costYoungThree 
    global costYoungFourUp

    global costZero
    global costOne
    global costTwo
    global costThree
    global costFourUp
    
    pricePoint = costYoungZero
    
    if bracket == "youngzero":
        pricePoint == costYoungZero
        name = "young people with 0 offenses"
    elif bracket == "youngone":
        pricePoint == costYoungOne
        name = "young people with 1 offense"
    elif bracket == "youngtwo":
        pricePoint == costYoungTwo
        name = "young people with 2 offenses"
    elif bracket == "youngthree":
        pricePoint == costYoungThree
        name = "young people with 3 offenses"
    elif bracket == "youngfour":
        pricePoint == costYoungFourUp
        name = "young people with 4 or more offenses"
    elif bracket == "zero":
        pricePoint = costZero
        name = "people with 0 offenses"
    elif bracket == "one":
        pricePoint == costOne
        name = "people with 1 offense"
    elif bracket == "two":
        pricePoint == costTwo
        name = "people with 2 offenses"
    elif bracket == "three":
        pricePoint == costThree
        name = "people with 3 offenses"
    elif bracket == "four":
        pricePoint == costFourUp
        name = "people with 4 or more offenses"
        
    correct = False
    while correct == False:
        print("What would you like the price for", name, "to be?")
        print("(Type \'back\' to go back)")
        pricePoint = str.lower(input("$"))
        if pricePoint == "back":
            return("0")
        elif pricePoint == "quit":
            return("quit")
        else:
            pricePoint = inValid5.posFloatValid(pricePoint,"")
            if pricePoint == "quit":
                return("quit")
            message = "The new price point is now $" + str(pricePoint) + " for " + name + " is this correct? Y/N"
            correct = input(message)
            correct = inValid5.boolValid(correct, "")
        
        if correct == True:
            if bracket == "youngzero":
                costYoungZero = pricePoint
                return("0")
            elif bracket == "youngone":
                costYoungOne = pricePoint
                return("0")
            elif bracket == "youngtwo":
                costYoungTwo = pricePoint
                return("0")
            elif bracket == "youngthree":
                costYoungThree = pricePoint
                return("0")
            elif bracket == "youngfour":
                costYoungFourUp = pricePoint
                return("0")
            elif bracket == "zero":
                costZero = pricePoint
                return("0")
            elif bracket == "one":
                costOne = pricePoint
                return("0")
            elif bracket == "two":
                costTwo = pricePoint
                return("0")
            elif bracket == "three":
                costThree = pricePoint
                return("0")
            elif bracket == "four":
                costFourUp = pricePoint
                return("0")
            return("1")
        elif correct == "quit" or pricePoint == "quit":
            return("quit")
            correct = True
        else:
            correct = False
