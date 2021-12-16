import math

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
    "money": 0
}

PENNY = .01
NICKLE = .05
DIME = .10
QUARTER = .25


def print_report():
    """Retrieves current resource state then formats and prints to the console"""
    machine_water = resources["water"]
    machine_milk = resources["milk"]
    machine_coffee = resources["coffee"]
    machine_money = resources["money"]

    print(f"{machine_water=}\n{machine_milk=}\n{machine_coffee=}\n{machine_money=}")


def order_prompt():
    """Prompt user for instructions and returns instructions as a string"""
    order = input("What would you like?: 1=espresso, 2=latte, 3=cappuccino: ").lower()

    if order == "1":
        return "espresso"
    if order == "2":
        return "latte"
    if order == "3":
        return "cappuccino"
    if order == "off" or order == "Off":
        return "off"
    elif order == "report":
        return "report"
    else:
        return order


def complete_payment(order):
    payment_processing = 1
    balance = float(MENU[order]["cost"])
    payment = 0
    coin = 0
    print(f"Balance: {balance}")
    while balance > 0.0:
        coin = int(input("Please insert coins: 1=1cent, 2=5cents 3=10cents 4=25cents "))
        if coin == 1:
            balance -= PENNY
            payment += PENNY
        elif coin == 2:
            balance -= NICKLE
            payment += NICKLE
        elif coin == 3:
            balance -= DIME
            payment += DIME
        elif coin == 4:
            balance -= QUARTER
            payment += QUARTER
        else:
            print("Invalid Tender")

        print(f"Balance: {round(balance, 2)}")
        # payment_processing = int(input("Still paying? 1=yes, 0=no: "))
    if balance > 0:
        return 0.0
    else:
        return payment


def check_resources(order):
    """Checks resource state to check if there are sufficient resources to make the selected drink"""
    missing = []
    # extract ingredients for given drink order. drink_ingredients is a dict
    drink_ingredients = MENU[order]["ingredients"]
    # loop through drink_ingredients and compare each value to the resources value.
    # both dicts use same key
    for key in drink_ingredients:
        if resources[key] < drink_ingredients[key]:
            missing.append(key)
    return missing


machine_on = True

while machine_on:
    # Get user command
    drink_order = order_prompt()

    if drink_order == "espresso" or drink_order == "latte" or drink_order == "cappuccino":
        # Check there are sufficient ingredient amounts to make drink order
        insufficient_resource = check_resources(drink_order)
        if not insufficient_resource:
            # process payment. If balance is paid returns the payment amount else returns 0
            completed_payment = complete_payment(drink_order)
            print(completed_payment)
            if completed_payment:
                # If payment was completed (make drink) "subtract required ingredients from resources"
                for resource in MENU[drink_order]["ingredients"]:
                    resources[resource] -= MENU[drink_order]["ingredients"][resource]
                    # Once loop reaches "money"
                resources["money"] += completed_payment
                print(f"Here is your {drink_order}. Enjoy :)")
            else:
                print(f"payment was not completed. Goodbye")
        else:
            print(f"Not enough {insufficient_resource}. Sorry")

    elif drink_order == "report":
        print_report()
    elif drink_order == "off":
        machine_on = False
        print("Goodbye")

# TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.

# TODO 2: Turn off the Coffee Machine by entering “off” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.

# TODO 3: Print report

# TODO 4: Check resources sufficient?

# TODO 5. Process coins

# TODO 6: Check if transaction was successful

# TODO 7. Make Coffee.
