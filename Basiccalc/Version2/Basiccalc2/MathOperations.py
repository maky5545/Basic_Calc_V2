ValidOperations = ["+", "-", "/", "*"]

# Calculation taking two numbers and the arithmetic operation
def PerformOperation(no1, no2, ariv):
        # Addition
        if ariv == "+":
                sum = no1 + no2
        elif ariv == "-":
                sum = no1 - no2
        elif ariv == "/":
                sum = no1 / no2
        elif ariv == "*":
                sum = no1 * no2
        return sum
    
def FormatNumber(num):
        if num == int(num):
                return int(num)
        else:
                return float(num)

def FormatNumbers(numbers):
        returnValues = []
        for number in numbers:
                returnValues.append(FormatNumber(number))
        return returnValues

def ToFloats(numbers):
        returnValues = []
        for number in numbers:
                returnValues.append(float(number))
        return returnValues