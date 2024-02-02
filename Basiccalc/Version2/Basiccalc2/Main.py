# Imports
import re # Regular Expressions to split the text in the calculation
from Checks import noDecimal # Check if the number has a decimal part
from Checks import fileCreator # Check if directory and file exsists, if not, create them, then write the values to the files.
from Misc import clear_console # Clears the console
from Misc import fileLocation # Prints the location of the file
from Operators import add_numbers # Addition
from Operators import sub_numbers # Subtraction
from Operators import div_numbers # Division
from Operators import mul_numbers # Multiplication

# Define General Variables
mainLoop = True # Main program loop

# Intro Strings
print(str.center("Welcome to the calculator!", 50,))
print(str.center('Type "Exit" at any time to leave', 50,))

# Main Program Loop
while mainLoop == True:
    userCalc = input("\n" + "Please input the calculation: ").rstrip("\n") # variable for the user's calculation
    if userCalc == "Exit" or userCalc == "exit": # Exit the program if the user types "Exit"
        mainLoop = False # just for good mesure
        break # Exit the main program loop if the user types "Exit"
    
    # variable: split the input into 3 parts: number1, operation, number2
    firstNumber, operation, secondNumber = re.split(r'(\+|\-|\*|\/)', userCalc)

    # Convert the strings to integers or floats depending on if they have a decimal part
    if noDecimal(float(firstNumber)) == True:
        firstNumber = int(firstNumber)
    elif noDecimal(float(firstNumber)) == False:
        firstNumber = float(firstNumber)
    if noDecimal(float(secondNumber)) == True:
        secondNumber = int(secondNumber)
    elif noDecimal(float(secondNumber)) == False:
        secondNumber = float(secondNumber)

    # Main Program Logic using if statements
    if operation == "+": # Addition
        opAnswer = add_numbers(firstNumber, secondNumber)
        if noDecimal(opAnswer) == True: # Check if the answer has a decimal part
            
            print("\n" + str(firstNumber) + operation + str(secondNumber) + " = " + str(int(opAnswer))) # Print the answer to console
            fileCreator(firstNumber, secondNumber, operation, int(opAnswer)) # Write the answer to the file

        elif noDecimal(opAnswer) == False:
            print("\n" + str(firstNumber) + operation + str(secondNumber) + " = " + str(float(opAnswer))) # Print the answer to console
            fileCreator(firstNumber, secondNumber, operation, float(opAnswer)) # Write the answer to the file
    
    elif operation == "-":
        opAnswer = sub_numbers(firstNumber, secondNumber)
        if noDecimal(opAnswer) == True: # Check if the answer has a decimal part
            print("\n" + str(firstNumber) + operation + str(secondNumber) + " = " + str(int(opAnswer))) # Print the answer to console
            fileCreator(firstNumber, secondNumber, operation, int(opAnswer)) # Write the answer to the file

        elif noDecimal(opAnswer) == False:
            print("\n" + str(firstNumber) + operation + str(secondNumber) + " = " + str(float(opAnswer))) # Print the answer to console
            fileCreator(firstNumber, secondNumber, operation, float(opAnswer)) # Write the answer to the file

    elif operation == "/":
        opAnswer = div_numbers(firstNumber, secondNumber)
        if noDecimal(opAnswer) == True: # Check if the answer has a decimal part
            print("\n" + str(firstNumber) + operation + str(secondNumber) + " = " + str(int(opAnswer))) # Print the answer to console
            fileCreator(firstNumber, secondNumber, operation, int(opAnswer)) # Write the answer to the file

        elif noDecimal(opAnswer) == False:
            print("\n" + str(firstNumber) + operation + str(secondNumber) + " = " + str(float(opAnswer))) # Print the answer to console
            fileCreator(firstNumber, secondNumber, operation, float(opAnswer)) # Write the answer to the file
    
    elif operation == "*":
        opAnswer = mul_numbers(firstNumber, secondNumber)
        if noDecimal(opAnswer) == True: # Check if the answer has a decimal part
            print("\n" + str(firstNumber) + operation + str(secondNumber) + " = " + str(int(opAnswer))) # Print the answer to console
            fileCreator(firstNumber, secondNumber, operation, float(opAnswer)) # Write the answer to the file

        elif noDecimal(opAnswer) == False:
            print("\n" + str(firstNumber) + operation + str(secondNumber) + " = " + str(float(opAnswer))) # Print the answer to console
            fileCreator(firstNumber, secondNumber, operation, float(opAnswer)) # Write the answer to the file
    

clear_console()
print("Thank you for using the calculator.")
fileLocation()
input("Press enter to continue...")