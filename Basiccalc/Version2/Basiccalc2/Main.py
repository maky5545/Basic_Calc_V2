# Imports
from FileManagement import outputFileCreator, fileLocation, openFileLocation
from MathOperations import PerformOperation, FormatNumbers, ToFloats
from Misc import ParseInput

# Define General Variables
lineCounter = 1

# Intro Strings
print(str.center("Welcome to the calculator!", 50,))
print(str.center('Type "Exit" at any time to leave', 50,))

# Main Loop
while True:
    userCalc = input("\n" + "Please input the calculation: ").rstrip()
    if userCalc.lower() == "exit":
        break

    firstNumber, operator, secondNumber, errorMessage = ParseInput(userCalc)

    if errorMessage != "":
        print(errorMessage)
        continue

    firstNumber, secondNumber = ToFloats([firstNumber, secondNumber]) 

    opAnswer = PerformOperation(firstNumber, secondNumber, operator)

    firstNumber, secondNumber, opAnswer = FormatNumbers([firstNumber, secondNumber, opAnswer])

    print(f"\n{str(firstNumber)} {operator} {str(secondNumber)} = {opAnswer}")

    outputFileCreator(lineCounter, str(firstNumber), str(secondNumber), operator, round(opAnswer, 3))
    
    lineCounter += 1

