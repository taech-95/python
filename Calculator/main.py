from art import logo
print(logo)

def add(number1, number2):
    return float(number1+number2)
def substract(number1, number2):
    return float(number1-number2)
def multiply(number1, number2):
    return float(number1*number2)
def divide(number1, number2):
    return float(number1/number2)


functions = {
    "+": add, 
    "-": substract, 
    "*": multiply, 
    "/": divide}

def calculator():
    one_more_time = True
    num1 = float(input("Provide your first number: \n"))  
    print("Available operations:")
    for function in functions:
        print(function)
    while one_more_time:

        operation_function = input("Pick an operation from the line above: ")
        num2 = float(input("Provide your next number:\n"))
        calculation_function = functions[operation_function]
        answer = calculation_function(num1,num2)
        print(f"{num1}  {operation_function}  {num2} = {answer}")

        user_choise=input(f"Type 'y' to continue calculationg with {answer}, type 'new' for new calculation or type 'n' to exit:   ").lower()
        if user_choise=="n":
            one_more_time = False
        elif user_choise =="new":
            calculator()
        else:
            num1=answer
            
        
calculator()