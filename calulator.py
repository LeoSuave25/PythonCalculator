#Python Calculator
import pyfiglet as fig
print("\033[32m","="*100,"\033[m")
title = "Python Calculator"
print("\033[32m",fig.figlet_format(title),"\033[m")
print(fig.figlet_format("Made by: Leoj M Suaverdez",font="bubble"))
#Operation Methods
def add(first, second):
    return first + second

def subtract(first, second):
    return first - second

def multiply(first, second):
    return first * second

def divide(first, second):
    return first / second
def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("\033[1;31mInvalid input! Please enter a valid number.\033[0m")
#Ask the user to choose one of the four math operations (Addition, Subtraction, Multiplication and Division)
operations = {
    1: ("Addition", add),
    2: ("Subtraction", subtract),
    3: ("Multiplication", multiply),
    4: ("Division", divide),
}
response = "Y"
while response == "Y":
    print("Choose an operation:")
    for operation_num, (operation_name, _) in operations.items():
        print(f"({operation_num}) {operation_name}")

    while True:
        try:
            operation = int(input("Enter 1 | 2 | 3 | 4: "))
            if operation not in operations:
                raise ValueError("\033[1;31mInvalid operation! Please enter a valid operation number (1-4).\033[0m")
            break
        except ValueError as error:
                print(error)

    #Ask the user for two numbers
    print(f"You are now using \033[1;32m{operations[operation][0]}\033[0m")
    first_number = get_number_input("Enter the first number: ")
    second_number = get_number_input("Enter the second number: ")
    try:
        _, operation_function = operations[operation]
        result = operation_function(first_number, second_number)
    except ZeroDivisionError:
        print("\033[1;31mError: division by zero!\033[0m")
        continue
    #Display the result
    print("Result:", result)
    #Ask the user if the users wants to try again or not
    #If yes, repeat Step 1
    while True:
        try:
            response = input("Do you want to try again? Y/N: ").upper()
            if response not in {"Y","N"}:
                raise ValueError("\033[1;31mInvalid Response! Please enter a valid Letter.\033[0m")
            break
        except ValueError as error:
                print(error)
#If no, display thank you
print("\033[1;32mThank You!\033[0m")
print("\033[32m","="*100,"\033[m")
#Use Python Function and appropriate Exceptions to capture errors during runtime.