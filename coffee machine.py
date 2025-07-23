MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

COST_ESPRESSO = MENU["espresso"]["cost"]
COST_LATTE = MENU["latte"]["cost"]
COST_CAPUCCINO = MENU["cappuccino"]["cost"]

#TODO 1 Need to prompt user by asking what do u want;-

def requirement():
    want = input("what do u like to have espresso,latte,cappuccino? ")
    return want

#TODO 2 turning off the coffee machine:-

def off(maintanance):
    if maintanance == "y":
        return False
    else:
        return True

#TODO 3 PRINT REPORT

def report():
        print(f"the amount of water is {resources['water']}")
        print(f"the amount of milk is {resources['milk']}")
        print(f"the amount of coffee is {resources['coffee']}")

#TODO 4 check whether sufficient recourse are avaliable for the user's choice of drink

def avaResources(drink):

    actualWater = resources["water"]
    actualMilk = resources["milk"]
    actualCoffee = resources["coffee"]

    if drink == "espresso":
        water = MENU["espresso"]["ingredients"]["water"]
        coffee = MENU["espresso"]["ingredients"]["coffee"]

        if water > actualWater:
            print("there is no sufficient water")
        elif coffee > actualCoffee:
            print("there is no sufficient milk")
        else:
            print("Pay 1.5 ")

    elif drink == "latte":
        milk = MENU["latte"]["ingredients"]["milk"]
        coffee = MENU["latte"]["ingredients"]["coffee"]
        water = MENU["latte"]["ingredients"]["water"]

        if milk > actualMilk:
            print("there is no sufficient milk")
        elif coffee > actualCoffee:
            print("there is no sufficient coffee")
        elif water > actualWater:
            print("there is no sufficient water")
        else:
            print("Pay 2.5")

    elif drink == "cappuccino":
        milk = MENU["cappuccino"]["ingredients"]["water"]
        coffee = MENU["cappuccino"]["ingredients"]["coffee"]
        water = MENU["cappuccino"]["ingredients"]["water"]

        if milk > actualMilk:
            print("there is no sufficient milk")
        elif coffee > actualCoffee:
            print("there is no sufficient coffee")
        elif water > actualWater:
            print("there is no sufficient water")
        else:
            print("Pay 3.0")

#TODO 5 process coins

def amount(quater,dime,nickle,penny):
    amtQuater = 0.25*quater
    amtDime = 0.10*dime
    amtNickle = 0.05*nickle
    amtPenny = 0.01*penny
    totalAmtUser =  amtDime+amtQuater+amtNickle+amtPenny
    return totalAmtUser


#TODO 6 check weather the transaction is sucessful or not

want_coffee = requirement()

avaResources(want_coffee)

noOfQuater = int(input("how many quaters do you have?"))
noOfDime = int(input("how many dimes do you have?"))
noOfNickle = int(input("how many nickles do you have?"))
noOfPenny = int(input("how many pennies do you have?"))

needToReturn = 0

def sucessTrans(choice):

    userMoney = amount(noOfQuater,noOfDime,noOfNickle,noOfPenny)

    if choice == "espresso":
        amt_req = COST_ESPRESSO
    elif choice == "latte":
        amt_req = COST_LATTE
    elif choice == "cappuccino":
        amt_req = COST_CAPUCCINO

    if userMoney < amt_req:
        print("you don't have enough money")
        return False
    elif userMoney > amt_req:
        needToReturn = userMoney - amt_req

    return(f"change{needToReturn}")

#TODO 7 Make coffee


def make_coffee():
    if sucessTrans(requirement()):
        print(f"remaining change is {sucessTrans(requirement())}")
    else :
        print("you don't have enough money")

    CHOICE_USER = requirement()

    if CHOICE_USER == "espresso":
        resources["water"] -= MENU["espresso"]["water"]
        resources["coffee"] -= MENU["espresso"]["coffee"]

    elif CHOICE_USER == "latte":
        resources["milk"] -= MENU["latte"]["milk"]
        resources["coffee"] -= MENU["latte"]["coffee"]
        resources["water"] -= MENU["latte"]["water"]

    elif CHOICE_USER == "cappuccino":
        resources["milk"] -= MENU["cappuccino"]["milk"]
        resources["water"] -= MENU["cappuccino"]["water"]
        resources["coffee"] -= MENU["cappuccino"]["coffee"]

    return f'''amt of milk left {resources["milk"]}
    f"amt of coffee left {resources["coffee"]} 
    amt of water left {resources["water"]}'''

sucessTrans(requirement())
print(sucessTrans(requirement()))
want_to_close = input("enter y if maintanance is going on")











