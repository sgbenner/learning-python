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

machine_money = 0

def print_report(resources, money):
    print(f"Water remaining: {resources['water']}ml")
    print(f"Milk remaining: {resources['milk']}ml")
    print(f"Cofee remaining: {resources['coffee']}g")
    print(f"Money received: ${money}")

def check_if_enough_resources(resources, drink):
    water_needed, milk_needed, coffee_needed = get_ingredients(drink)

    if resources["water"] - water_needed < 0:
        print("Sorry there is not enough water")
        return False
    elif resources["milk"] - milk_needed < 0:
        print("Sorry there is not enough milk")
        return False
    elif resources["coffee"] - coffee_needed < 0:
        print("Sorry there is not enough coffee")
        return False
    else:
        return True

def get_ingredients(drink):
    requested_drink = MENU[drink]
    ingredients = requested_drink["ingredients"]

    water_needed = ingredients.get("water", 0)
    milk_needed = ingredients.get("milk", 0)
    coffee_needed = ingredients.get("coffee", 0)

    return water_needed, milk_needed, coffee_needed

def use_resources(resources, drink):
    water_needed, milk_needed, coffee_needed = get_ingredients(drink)

    print(f"Resources needed: water - {water_needed} | milk - {milk_needed} | coffee - {coffee_needed}")

    resources["water"] = resources["water"] - water_needed
    resources["milk"] = resources["milk"] - milk_needed
    resources["coffee"] = resources["coffee"] - coffee_needed

def make_drink(resources, drink):
    use_resources(resources, drink)

    print(f"Here's your {drink}. Be careful, its hot!")

def get_drink_cost(requested_drink):
    return MENU[requested_drink]["cost"]

def menu_items():
    return list(MENU.keys())

def valid_input(requested_drink):
    if requested_drink in menu_items():
        return True
    else:
        return False

def get_money():
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickles = int(input("Nickles: "))
    pennies = int(input("Pennies: "))

    money_input = int((quarters * 25) + (dimes * 10) + (nickles * 5) + (pennies * 1)) / 100
    print(f"Total money received: {money_input}")

    return money_input

def get_change(drink_cost, money_received):
    return money_received - drink_cost

# Prompt user for what drink they would like
keep_going = True

while keep_going:
    requested_drink = input("Welcome to the coffee machine. What would you like? (espresso/latte/cappuccino): ")

    # If user enters report, print the report and end
    if requested_drink == "off":
        print("Goodbye")
        keep_going = False
    elif requested_drink == "report":
        print_report(resources, machine_money)
    elif not valid_input(requested_drink):
        print("Sorry, we don't serve that drink.")
    else:
        enough_resources = check_if_enough_resources(resources, requested_drink)

        if enough_resources:
            drink_cost = get_drink_cost(requested_drink)
            print(f"This drink costs: ${get_drink_cost(requested_drink)}")

            money_received = get_money()

            # Process Payment - if enough money, count it. Otherwise, bail out
            if money_received < drink_cost:
                print("Sorry, you did not insert enough money, please start over")
            else:
                # add money to machine
                machine_money += drink_cost

                # return change
                change_owed = get_change(drink_cost, money_received)
                if change_owed > 0:
                    print(f"Here's your change: {change_owed}")

                # Make Drink
                make_drink(resources, requested_drink)


