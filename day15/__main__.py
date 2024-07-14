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


def format_price(price_in_cents):
    return f"${'{:.2f}'.format(price_in_cents / 100)}"


def check_resources(ingredients):
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry there's no enough {ingredient}")
            return False
    return True


def process_coins(cost):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 25
    dimes = int(input("How many dimes?: ")) * 10
    nickles = int(input("How many nickles?: ")) * 5
    pennies = int(input("How many pennies?: ")) * 1

    input_cents = quarters + dimes + nickles + pennies
    if input_cents < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        if 'money' not in resources:
            resources['money'] = 0
        resources['money'] += cost
        change = input_cents - cost
        if change > 0:
            print(f"Here is {format_price(change)} in change.")
        return True


def reduce_resources(ingredients):
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]


def make_drink(drink: str):
    menu_item = MENU[drink]
    ingredients = menu_item["ingredients"]

    if not check_resources(ingredients):
        return

    if not process_coins(menu_item['cost'] * 100):
        return

    reduce_resources(ingredients)

    print(f"Here is your {drink} ☕ Enjoy!")


def print_report():
    for key in resources:
        if key == "water":
            print(f"Water: {resources[key]}ml")
        if key == "milk":
            print(f"Milk: {resources[key]}ml")
        if key == "coffee":
            print(f"Coffee: {resources[key]}g")
        if key == "money":
            print(f"Money: {format_price(resources[key])}")


def run_machine():
    turned_on = True
    while turned_on:
        answer = input("What would you like? (espresso/latte/cappuccino): ")
        if answer == "espresso" or answer == "latte" or answer == "cappuccino":
            make_drink(answer)
        elif answer == "off":
            turned_on = False
        elif answer == "report":
            print_report()


run_machine()
