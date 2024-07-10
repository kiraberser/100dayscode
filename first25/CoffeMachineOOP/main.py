from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeMaker = CoffeeMaker()
money = MoneyMachine()

run = True
while run:
    order = input(f"What would you like? {menu.get_items()}: ").lower()
    if order == "off":
        run = False
    elif order == "report":
        coffeMaker.report()
        money.report()
    else:
        coffe = menu.find_drink(order) 
        if coffeMaker.is_resource_sufficient(coffe):
            if money.make_payment(coffe.cost):
                coffeMaker.make_coffee(coffe)