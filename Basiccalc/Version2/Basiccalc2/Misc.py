# Imports
import os
import time
import re
from MathOperations import ValidOperations

# clears the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# sleeps the console for 2 seconds
def consoleSleep2():
    time.sleep(2)

def ParseInput(input):
    items = re.split(r'(\+|-|\*|/)', input)
    if len(items) != 3:
        return ["","","","Incorrect number of items in input"]

    return [items[0],items[1],items[2],""]