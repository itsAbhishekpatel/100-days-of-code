# there is endless possibility and approach to solve a problem 
from MENU import MENU, resources

profit = 0

# we are checking if order ingredinets is greter than or equal to resoureces or not 
def is_resources_sufficient(order_ingrident):
    """Retrun True when order can be made, False if ingredients are insufficient."""
    for item in order_ingrident:
        if order_ingrident[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True 

# Taking coin form the user and return total money 
def process_coin():
    """Return the total calculated from coin inserted."""
    print("Please insert the coin.")
    total = int(input("How many quaters?: "))*0.25
    total += int(input("How many dimes?: "))*0.10
    total += int(input("How many nickles?: "))*0.05
    total += int(input("How many pennies?: "))*0.01

    return total 

def is_transaction_successful(money_recived,drink_cost):
    """Return true when the payment is accepted, or False is money is refunded."""
    if money_recived > drink_cost:
        global profit
        profit += drink_cost
        change = round((money_recived - drink_cost),2)
        print(f"Here is ${change} in change")
        return True  
    else:
        print("Sorry that's is not enough money. Money refunded.")
        return False

def make_coffee(drink_name,order_ingredient):
    """Deduct the require ingedient form the resourses."""
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here is your coffe {drink_name}☕, Enjoy!")

while True:
    coffee = input("What would you like? (espresso/latte/cappuccino):")

    if coffee == "off":
        break
    elif coffee == "report":
        print(f"water: {resources["water"]}ml")
        print(f"milk: {resources["milk"]}ml")
        print(f"coffee: {resources["coffee"]}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[coffee]
        if is_resources_sufficient(drink["ingredient"]):
            payment = process_coin()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(coffee,drink["ingredient"])

                 
        

