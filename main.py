import menu

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def print_report():
    """Prints the current state of the machine's resources."""
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: £{resources["money"]:.2f}")

def check_resources(drink):
    """Checks if there is enough resources to make the drink."""
    for item in menu.MENU[drink]["ingredients"]:
        if menu.MENU[drink]["ingredients"][item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
        return True
    
def process_coins():
    """Prompts the user to insert the coins and calculates the total."""
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total

def check_transaction(money_received, drink_cost):
    """Checks is the money received is enough to buy the drink."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"Here is £{change} in change")
        resources["money"] += drink_cost
        return True
    else:
        print("Sorry, That's not enough money. Money Refunded.")

def make_drink(drink):
    """Deducts the ingredients from the resources and makes the drink."""
    for item in menu.MENU[drink]["ingredients"]:
        resources[item] -= menu.MENU[drink]["ingredients"][item]
    print(f"Here is your {drink}. Enjoy!.")



