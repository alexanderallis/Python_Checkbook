import inValid5
import calculations

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

def getFirstName():
    message = "Please input the first name: "
    name = input(message)
    return(inValid5.nameValid(name, message))

def getLastName():
    message = "Please input the last name: "
    name = input(message)
    return(inValid5.nameValid(name, message))

def getAge():
    age = (input("Please input your age: "))
    return(inValid5.rangeValid(age, 16, 105))

def getViolations():
    message = "Please input the number of traffic violations you have received: "
    violations = input(message)
    return(inValid5.posIntValid(violations, message))

def riskType(vio):
    riskType = ""
    if vio == 0:
        riskType = "no"
    elif vio == 1:
        riskType = "low"
    elif vio == 2 or vio == 3:
        riskType = "moderate"
    else:
        riskType = "high"
    return(riskType)


def main():
    global breakPoint
    firstName = getFirstName()
    if firstName == "quit":
        return("0")
    surname = getLastName()
    if surname == "quit":
        return("0")
    age = getAge()
    if age == "quit":
        return("0")
    vio = getViolations()
    if vio == "quit":
        return("0")
    risk = riskType(vio)
    breakPoint = breakPoint
    cost = calculations.getCalculations(age, vio)
    reply = firstName + " " + surname + ", as a " + risk + " risk driver, your insurance will cost $" + str(cost)
    print(reply)
    userQuit = input("Good job there, big shot, you wanna go again?")
    userQuit = (inValid5.boolValid(userQuit, ""))
    if userQuit == True:
        return("1")
    else:
        return("0")
    
def meta():
    status = menu("0")
    while status == "0" or status == "1":
        status = menu(status)
        
    print("goodbye")

def menu(choice):
    if choice == "0":
        print("Choose an option")
        print("1 = Run Program")
        print("2 = Admin")
        print("3 = Quit")
        choice = input("")
        choice = inValid5.rangeValid(choice, 1, 3)
    else:
        x=2
    if choice == 1 or choice == "1":
        return (main())
    elif choice == 2 or choice == "2":
        return (calculations.adminMeta("0"))
    else:
        return ("quit")

meta()
