from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def run_machine():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    turned_on = True
    while turned_on:
        answer = input(f"What would you like? ({menu.get_items()}): ")
        if answer == "off":
            turned_on = False
        elif answer == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(answer)
            if drink is not None:
                if coffee_maker.is_resource_sufficient(drink):
                    if money_machine.make_payment(drink.cost):
                        coffee_maker.make_coffee(drink)


run_machine()
