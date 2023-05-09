#Python Calculator
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
            print("Invalid input! Please enter a valid number.")
#Ask the user to choose one of the four math operations (Addition, Subtraction, Multiplication and Division)
operations = {
    1: ("Addition", add),
    2: ("Subtraction", subtract),
    3: ("Multiplication", multiply),
    4: ("Division", divide),
}
print("Choose an operation:")
for operation_num, (operation_name, _) in operations.items():
    print(f"({operation_num}) {operation_name}")
operation = int(input("Enter 1 | 2 | 3 | 4: "))
#Ask the user for two numbers
first_number = get_number_input("Enter the first number: ")
second_number = get_number_input("Enter the second number: ")
#Display the result
_, operation_function = operations[operation]
result = operation_function(first_number, second_number)
print("Result:", result)
#Ask the user if the users wants to try again or not
#If yes, repeat Step 1
#If no, display thank you
#Use Python Function and appropriate Exceptions to capture errors during runtime.