from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


is_on= True
while is_on:
    options = menu.get_items()
    user_choice = input(f"What would you like? {options}").lower()
    if user_choice == "exit":
        is_on = False
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.profit()
    else:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink):
            if (money_machine.make_payment(drink.cost)):
                coffee_maker.make_coffee(drink)
