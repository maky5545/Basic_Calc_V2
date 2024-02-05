# Imports
import re
from FileManagement import outputFileCreator, fileLocation, openFileLocation
from MathOperations import calcOperations, convert_to_number
from Misc import clear_console, consoleSleep2

# Define General Variables
operations = ["+", "-", "/", "*"]
lineCounter = 1

# Intro Strings
print(str.center("Welcome to the calculator!", 50,))
print(str.center('Type "Exit" at any time to leave', 50,))

# Main Loop
while True:
    userCalc = input("\n" + "Please input the calculation: ").rstrip()
    # Check if user wants to exit
    if userCalc.lower() == "exit":
        break

    try:
        firstNumber, operator, secondNumber = re.split(r'(\+|-|\*|/)', userCalc)        
        firstNumber, secondNumber = convert_to_number(firstNumber), convert_to_number(secondNumber)
    except ValueError:
        input("\033[1;31mERROR: Invalid input, press enter to try again.\033[0m")
        clear_console()
        continue    

    if operator not in operations:
        input("\033[1;31mERROR: Invalid operation, press enter to try again.\033[0m")
        clear_console()
        continue
        
    while True:
        if operator in operations:
            opAnswer = calcOperations(firstNumber, secondNumber, operator)
            convert_to_number(opAnswer)
            break
        else:
            input("\033[1;31mERROR: Invalid operation, press enter to try again.\033[0m")
            clear_console()
            resetLoop = True
            continue
    
    print(f"\n{firstNumber} {operator} {secondNumber} = {round(opAnswer, 3)}")
    outputFileCreator(lineCounter, firstNumber, secondNumber, operator, round(opAnswer, 3))
    lineCounter += 1