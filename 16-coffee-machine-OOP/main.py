# import necessary classes
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# instantiate objects of all required classes
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# The coffee_machine is initially ON
is_on = True

while is_on:
    # get available options on the menu
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        # check if ingredients will suffice to prepare the requested drink
        is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        # check if payment is successful
        is_payment_successful = money_machine.make_payment(drink.cost)
        # proceed to make coffee!
        if is_enough_ingredients and is_payment_successful:
            coffee_maker.make_coffee(drink)

