from Day_11.art import logo


def add(num1,num2):
    return num1+num2

def mul(num1,num2):
    return num1*num2

def subs(num1,num2):
    return num1-num2

def div(num1,num2):
    return num1/num2

operations = {
    "+" : add,
    "-" : subs,
    "*" : mul,
    "/" : div
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number? : "))

    for sysmbol in operations:
        print(sysmbol)

    should_countinue = True

    while should_countinue:
        operation_symbol = input("Pick an operation : ")
        num2 = float(input("what's the next number? : "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to countinue calculation with {answer}, or type n to start new calculation ") == 'y':
                num1 = answer
        
        else:
            should_countinue = False
            calculator()

calculator()


