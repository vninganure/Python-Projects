MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    "money": 0
}


def report():
    for i in resources:
        if i == 'coffee':
            print(f"{i}: {resources[i]}g")
        elif i == 'money':
            print(f"{i}: ${resources[i]}")
        else:
            print(f"{i}: {resources[i]}ml")


def coin_insert():
    print("Please insert the coin.")
    quarters = int(input("How many quarters? :"))
    dime = int(input("How many dime? :"))
    nickels = int(input("How many nickels? :"))
    pennies = int(input("How many pennies? :"))
    total_coins = quarters*0.25+dime*0.10+nickels*0.05+pennies*0.01
    return total_coins


def is_sufficient(coins, amount, resources):
    if coins < amount["cost"]:
        return "coins insufficient, money refunded"
    elif resources["water"] < amount["ingredients"]["water"]:
        return "Sorry, There is not enough water."
    elif resources["coffee"] < amount["ingredients"]["coffee"]:
        return "Sorry, There is not enough water."
    elif resources["milk"] < amount["ingredients"]["milk"]:
        return "Sorry, There is not enough milk."


def sufficient(coins, amount, resources):
    if amount["cost"] < coins:
        refund = coins - amount["cost"]
    resources["money"] += amount["cost"]
    resources["water"] -= amount["ingredients"]["water"]
    resources["coffee"] -= amount["ingredients"]["coffee"]
    resources["milk"] -= amount["ingredients"]["milk"]
    return refund


def get_coffee(espresso, resources):
    coins = coin_insert()
    reason = is_sufficient(coins, espresso, resources)
    if not reason:
        refund = sufficient(coins, espresso, resources)
        print(f"Here is {refund} in change")
        print("Here is your espresso, Enjoy")
    else :
        print(reason)


should_continoue = True
while should_continoue:
    inp = input("What would you like? (espresso/latte/cappuccino)").lower()
    if inp == 'report':
        report()
    elif inp == 'espresso':
        get_coffee(MENU["espresso"], resources)
    elif inp == 'latte':
        get_coffee(MENU["latte"], resources)
    elif inp == 'cappuccino':
        get_coffee(MENU["cappuccino"], resources)
    elif inp == 'off':
        should_continoue = False
