# Imports
import re
from FileManagement import outputFileCreator, fileLocation, openFileLocation
from MathOperations import calcOperations, noDecimal, convert_to_number
from Misc import clear_console, consoleSleep2

# Define General Variables
operations = ["+", "-", "/", "*"]

# Intro Strings
print(str.center("Welcome to the calculator!", 50,))
print(str.center('Type "Exit" at any time to leave', 50,))

while True:
    userCalc = input("\n" + "Please input the calculation: ").rstrip()
    if userCalc.lower() == "exit":
        break

    try:
        firstNumber, operator, secondNumber = userCalc.split()
        firstNumber, secondNumber = convert_to_number(firstNumber), convert_to_number(secondNumber)
    except ValueError:
        print("\033[1;31mERROR: Invalid input, press enter to try again.\033[0m")
        clear_console()
    
    if operator not in operations:
        print("\033[1;31mERROR: Invalid operation, press enter to try again.\033[0m")
        clear_console()
        
    while True:
        if operator in operations:
            opAnswer = calcOperations(firstNumber, secondNumber, operator)
            break
        else:
            print("\033[1;31mERROR: Invalid operation, press enter to try again.\033[0m")
            clear_console()
            resetLoop = True
            break
    
    print(f"\n{firstNumber} {operator} {secondNumber} = {opAnswer}")
    outputFileCreator(firstNumber, secondNumber, operator, opAnswer)
        

