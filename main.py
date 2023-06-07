from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money_machine = MoneyMachine()
my_coffe_report = CoffeeMaker()
menu = Menu()

while True:
    options = menu.get_items()
    choice = input(f"What would you like : {options} ?")

    if choice == "off":
        break
    elif choice == "report":
        my_money_machine.report()
        my_coffe_report.report()
    else:
        drink = menu.find_drink(choice)
        if my_coffe_report.is_resource_sufficient(drink):
            if my_money_machine.make_payment(drink.cost):
                my_coffe_report.make_coffee(drink)

