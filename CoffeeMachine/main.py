
money =0

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
}#
#TODO Create a report which will show how much resources do we have
def printReport(resources,money):
    report_water = resources["water"]
    report_milk = resources["milk"]
    report_coffee = resources["coffee"]
    print(f"Water: {report_water}")
    print(f"Milk: {report_milk}")
    print(f"Coffee: {report_coffee}")
    print(f"Money: ${money }")

# printReport(resources,money)

#Todo Function which will serve menu
def serve_menu(user_choise):
    if user_choise == "cappucino" or user_choise =="espresso" or user_choise =="latte":
        process_coins()
    elif user_choise == "report":
        printReport(resources, money)
    else:
        print("Wrong :(")



#Todo Create functions which will check sufficient resources
# def resources_sufficient(resources, order):
#
#     if True:
#         return True
#     else:
#         return False



#Todo Create function which will processes coins
def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?:  "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("how many pennies?: "))
    sum_of_coins = quarters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01
    print(f"Here is ${sum_of_coins} in change")




user_choise = input("What would you like? (espresso/latte/cappucino): ").lower()
serve_menu(user_choise)