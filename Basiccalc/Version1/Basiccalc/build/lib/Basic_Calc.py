import os
import re

# Define Variables
number1, operation, number2 = float(), float(), float()
userOperation = str(number1) + " " + str(operation) + " " + str(number2)
anotherOperationBoolean = True
anotherOperationStatement = str()

# Define Functions
# Addition
def add_numbers(a, b):
    sum = a + b
    return sum

# Subtraction
def sub_numbers(a, b):
    sum = a - b
    return sum

# Division
def div_numbers(a, b):
    sum = a / b
    return sum

# Multiplication
def mul_numbers(a, b):
    sum = a * b
    return sum

def check_if_integer(a):
    if a.is_integer():
        return True
    else:
        return False
    
# Debug Mode
def debug_mode():
    print("Debug Mode")
    print("Number 1: " + str(number1))
    print("Operation: " + str(operation))
    print("Number 2: " + str(number2))
    print("User Operation: " + str(userOperation))
    print("Another Operation Boolean: " + str(anotherOperationBoolean))
    print("Another Operation Statement: " + str(anotherOperationStatement))
    print("")

# Main Program Logic Loop Statement
while anotherOperationBoolean == True:

    # Main Program Logic just using if statements

    #number1, operation, number2 = input("Please enter the calculation: ").split()

    calculation = input("Please enter the calculation: ")

    # Split the input into 3 parts: number1, operation, number2
    number1, operation, number2 = re.split(r'(\+|\-|\*|\/)', calculation)
    number1 = float(number1)
    number2 = float(number2)

    

    # Convert the numbers to integers or floats

    if check_if_integer(number1) == True:
        number1 = int(number1)
    elif check_if_integer(number1) == False:
        number1 = float(number1)
    else:
        print("The input is not a number.")

    #print(number1)
    #print(number1.is_integer())
    #input("\n" + "...")

    if check_if_integer(number2) == True:
        number2 = int(number2)
    elif check_if_integer(number2) == False:
        number2 = float(number2)
    else:
        print("The input is not a number.")

    #displays the operation
    #input("Operation: " + str(operation))

    # if addition
    if operation == "+":
        print("\n" + "The answer is: ")
        print(add_numbers((number1), (number2)))

    # if subtraction
    elif operation == "-":
        print("\n" + "The answer is: ")
        print(sub_numbers((number1), (number2)))

    # if division
    elif operation == "/":
        print("\n" + "The answer is: ")
        print(div_numbers((number1), (number2)))

    # if multiplication
    elif operation == "*":
        print("\n" + "The answer is: ")
        print(mul_numbers((number1), (number2)))

    # variable that asks the user if they would like to do another operation
    anotherOperationStatement = input("\n" + "Would you like to do another operation? (y/n): ")
    
    # if the user does not want to do another operation
    if anotherOperationStatement == "n":
        
        anotherOperationBoolean = False
        
    # if the user does want to do another operation
    elif anotherOperationStatement == "y":
        
        # set variable to true (exits the loop)
        anotherOperationBoolean = True
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console

# End of Main Program Logic Loop Statement
input("\n" + "\033[1;31mPress enter to leave\033[0m")
# exit the program
exit()
# End of Program