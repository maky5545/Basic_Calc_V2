# Imports
import re # Regular Expressions to split the text in the calculation
from Checks import noDecimal # Check if the number has a decimal part
from Checks import fileCreator # Check if directory and file exsists, if not, create them, then write the values to the files.
from Misc import clear_console # Clears the console
from Misc import fileLocation # Prints the location of the file
from Misc import openFileLocation # Opens the file location
from Misc import consoleSleep2 # Sleeps the console for 2 seconds
from Operators import add_numbers # Addition
from Operators import sub_numbers # Subtraction
from Operators import div_numbers # Division
from Operators import mul_numbers # Multiplication

# Define General Variables
mainLoop = True # Main program loop
loopCount = 0 # Loop counter
userInput = False # User input loop
exitProg = False # Exit the program
firstNumber, operation, secondNumber = 0, "", 0 # Variables for the user's calculation

# Intro Strings
print(str.center("Welcome to the calculator!", 50,))
print(str.center('Type "Exit" at any time to leave', 50,))

# Main Program Loop
while mainLoop == True:
    while userInput == False:                    
        userCalc = input("\n" + "Please input the calculation: ").rstrip() # variable for the user's calculation
        if userCalc.lower() == "exit":
            exitProg = True
            break
        else:
            try:
                # variable: split the input into 3 parts: number1, operation, number2
                firstNumber, operation, secondNumber = re.split(r'(\+|\-|\*|\/)', userCalc)
                userInput = True # Exit the user input loop
            except ValueError:
                if operation != "+" or operation != "-" or operation != "*" or operation != "/":
                    input("\033[1;31mERROR: Invalid input, press enter to try again.\033[0m")
                    clear_console()
                    userInput = False # Re-enter the user input loop
                else:
                    input("\033[1;31mVALUE ERROR: \033[0m" + "Too many or too few values, press enter to try again.")
                    clear_console()
                    userInput = False # Re-enter the user input loop
                    
    
    # Exit the loop if the user types "Exit or exit"
    if exitProg == True:
        break

    # Convert the strings to integers or floats depending on if they have a decimal part
    if noDecimal(float(firstNumber)) == True:
        firstNumber = int(firstNumber)
    elif noDecimal(float(firstNumber)) == False:
        firstNumber = float(firstNumber)
    if noDecimal(float(secondNumber)) == True:
        secondNumber = int(secondNumber)
    elif noDecimal(float(secondNumber)) == False:
        secondNumber = float(secondNumber)

    if operation == "+":
        opAnswer = add_numbers(firstNumber, secondNumber)
    elif operation == "-":
        opAnswer = sub_numbers(firstNumber, secondNumber)
    elif operation == "/":
        opAnswer = div_numbers(firstNumber, secondNumber)
    elif operation == "*":
        opAnswer = mul_numbers(firstNumber, secondNumber)

    
    # Main Program Logic using if statements
    if noDecimal(opAnswer) == True: 
        print(f"\n{firstNumber} {operation} {secondNumber} = {int(opAnswer)}")
        fileCreator(firstNumber, secondNumber, operation, int(opAnswer))
    else:
        print(f"\n{firstNumber} {operation} {secondNumber} = {float(opAnswer)}")
        fileCreator(firstNumber, secondNumber, operation, float(opAnswer))

    loopCount += 1 # Increment the loop counter   
    userInput = False # To Restart The Loop    

# Exiting Program Stuff (Print output to the user, if a file was written gives the user it's location, then exits.)
clear_console() # Clearing Console           
print("Thank you for using the calculator.") 
if loopCount > 0:                      
    fileLocation()                           
    if input("\nWould you like to open the folder? (y/n): ").lower() == "y":
        openFileLocation()
        print("\nFile location opened. Exiting program...")
        consoleSleep2()
        exit()
    else:
        print("\nExiting program...")
        consoleSleep2()
        exit()        # >