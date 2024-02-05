# Calculation taking two numbers and the arithmetic operation
def calcOperations(no1, no2, ariv):
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

# Check if the number has a decimal part
def noDecimal(inoCheck):
    if inoCheck % 1 == 0:
        return True
    elif inoCheck % 1 != 0:
        return False
    
def convert_to_number(num):
    return int(num) if noDecimal(float(num)) else float(num)