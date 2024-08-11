from art import logo
print(logo)

def calc(first_num,sec_num,opr):
    if opr == "+":
        return first_num+sec_num
    elif opr == "-":
        return first_num-sec_num
    elif opr == "*":
        return first_num*sec_num
    elif opr == "/":
        return first_num/sec_num
    
flag = False

while not flag:
    num1 = int(input("What is first number? :  "))
    print("+","\n-","\n*","\n/")
    opr = input("Pick an operation: ")
    num2 = int(input("What is your next number? : "))
    result = calc(num1,num2,opr)
    print(f"{num1} {opr} {num2 } = {result}")

    should_countinue = input(f"Type 'y' to countinue with {result}, ot type no to start a new calculation.")
    
    next_flag = True
    while next_flag:
        if should_countinue == "y":
            opr = input("Pick an operation: ")
            num2 = int(input("What is your next number? : "))
            result = calc(result,num2,opr)
            print(f"{num1} {opr} {num2 } = {result}")

            should_countinue = input(f"Type 'y' to countinue with {result}, ot type no to start a new calculation.")

            if should_countinue == 'no':
                next_flag = False

