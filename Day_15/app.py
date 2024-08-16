# generate report of the resourses 
def report():
    if coffee == "report":
        print(f"water: {resources["water"]}ml")
        print(f"milk: {resources["milk"]}ml")
        print(f"coffee: {resources["coffee"]}g")
        print(f"money: ${resources["money"]}")

# take money from the user
def money():
    print("Please insert the coin.")
    quaters = (int(input("How many quaters?: ")))*0.25
    dimes = (int(input("How many dimes?: ")))*0.10
    nickles = (int(input("How many nickles?: ")))*0.05
    pennies = (int(input("How many pennies?: ")))*0.01

    total_money = round(quaters + dimes + nickles + pennies,2)
    return total_money

def update_res():
    if coffee == "expresso":
        resources["water"] = resources["water"] - 50
        resources["coffee"] = resources["coffee"] - 18
        resources["money"] = resources["money"] + 1.5

    if coffee == "latte":
        resources["water"] = resources["water"] - 200
        resources["coffee"] = resources["coffee"] - 24
        resources["milk"] = resources["milk"] - 150
        resources["money"] = resources["money"] + 2.5

    if coffee == "cappuccino":
        resources["water"] = resources["water"] - 250
        resources["coffee"] = resources["coffee"] - 24
        resources["milk"] = resources["milk"] - 100
        resources["money"] = resources["money"] + 3


# make the coffee and check the money
def which_coffee():
    total_money = money()
    if coffee == "expresso":
        if total_money >= 1.5:
            if resources["water"] >= 50 and resources["coffee"] >= 18:
                print(f"Here is ${total_money - 1.5} in change.")
                print("Here is your expresso Enjoy!")
                update_res()
            else:
                print(report())

        else:
            print("Sorry! Not Enough Money")

    elif coffee == "latte":
        if total_money >= 2.5:
            if resources["water"] >= 200 and resources["coffee"] > 24 and resources["milk"]>=150:
                print(f"Here is ${total_money - 2.5} in change.")
                print("Here is your latte Enjoy!")
                update_res()
            else:
                print(report())
        else:
            print("Sorry! Not Enough Money")

    elif coffee == "cappuccino":
        if total_money >= 3:
            if resources["water"] >= 250 and resources["coffee"] > 24 and resources["milk"]>=100:
                print(f"Here is ${total_money - 3} in change.")
                print("Here is your cappuccino Enjoy!")
                update_res()
            else:
                print(report())
        else:
            print("Sorry! Not Enough Money")


# take user input to decicde what coffee he want 

# print report 
resources = {
    "water" : 300,
    "milk" : 200,
    "coffee": 100,
    "money": 0
}
# print report of current resources 

# check resources if sufficient or not 

# process coin and return the change 
status = True
# Looping in the program
while status:
    coffee = input("What would you like? (espresso/latte/cappuccino):") 
    if coffee == "off":
        status = False
    elif coffee == "report":
        report()
    else:
        which_coffee()
# make a coffe after sucessful transaction 


