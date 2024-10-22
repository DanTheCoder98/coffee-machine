from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine():
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()

    is_on = True

    while is_on:
        options = menu.get_items()
        user_choice = input(f"What would you like? ({options}): ").lower()

        if user_choice == "off":
            is_on = False
        elif user_choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(user_choice)
            if drink:
                if coffee_maker.is_resource_sufficient(drink):
                    if money_machine.make_payment(drink.cost):
                        coffee_maker.make_coffee(drink)

coffee_machine()