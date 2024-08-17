from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# 1. print report
# 2. check resourse sufficent
# 3. process coin 
# 4. check transaction successful
# 5. make coffee 
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

while True:   
    options = menu.get_items()
    coffee = input(f"What would you like? ({options}):")
    if coffee == "off":
        break # exit to the loop if off is user input 
    elif coffee == "report":
        coffee_maker.report() # getthe report of the coffee
        money_machine.report() # get the status of the money
    else:   
        drink = menu.find_drink(coffee)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

    # Revision is most important thing so pls Do not forget to review occasinally