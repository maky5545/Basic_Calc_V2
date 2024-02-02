import os
from Checks import calcFileDirec, fileName

def fileLocation():
    print("A calculation files with all of the equations and answers has"
       " been created here: " + "\n" + calcFileDirec + fileName)


# clears the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
