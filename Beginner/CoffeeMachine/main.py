
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
}#

money =0
#TODO Create a report which will show how much resources do we have
def printReport(resources):
    report_water = resources["water"]
    report_milk = resources["milk"]
    report_coffee = resources["coffee"]
    report_money=resources["money"]
    print(f"Water: {report_water}")
    print(f"Milk: {report_milk}")
    print(f"Coffee: {report_coffee}")
    print(f"Money: ${report_money }")

# printReport(resources,money)



#Todo Function which will serve menu
def serve_menu(user_choise):
    money =0
    if user_choise == "cappuccino" or user_choise =="espresso" or user_choise =="latte":
        enough_resources=resources_sufficient(resources,user_choise)
        if(enough_resources):
            money = process_coins()
            water_from_order = MENU[user_choise]["ingredients"]["water"]
            coffee_from_order = MENU[user_choise]["ingredients"]["coffee"]
            milk_from_order = MENU[user_choise]["ingredients"]["milk"]
            resources["water"]-=water_from_order
            resources["coffee"]-=coffee_from_order
            resources["milk"]-=milk_from_order
            print(f"Here is ${money} in change")
            if money>MENU[user_choise]["cost"]:
                resources["money"]+=(MENU[user_choise]["cost"])
                print(f"Here is your {user_choise}! Enjoy")
            else:
                print("Sorry there is not enough money")
    elif user_choise == "report":
        printReport(resources)
    else:
        print("Wrong :(")


print(MENU["cappuccino"]["cost"])
#Todo Create functions which will check sufficient resources
def resources_sufficient(resources, order):
    water_from_order = MENU[order]["ingredients"]["water"]
    coffee_from_order = MENU[order]["ingredients"]["coffee"]
    milk_from_order = MENU[order]["ingredients"]["milk"]
    if resources["water"]>=water_from_order and resources["coffee"]>= coffee_from_order and resources["milk"]>=milk_from_order:

        return True
    elif resources["water"]<water_from_order:
        print("Sorry there is not enough water")
        return False
    elif resources["milk"] < milk_from_order:
        print("Sorry there is not enough milk")
        return False
    else:
        print("Sorry there is not enough coffee")
        return False



#Todo Create function which will processes coins
def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?:  "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("how many pennies?: "))
    sum_of_coins = quarters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01
    return sum_of_coins


user_input_flag = True
while user_input_flag:
    user_choise = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choise=="exit":
        user_input_flag=False
    else:
        serve_menu(user_choise)
