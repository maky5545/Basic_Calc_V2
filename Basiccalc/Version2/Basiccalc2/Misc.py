import os
from Checks import calcFileDirec, fileName
import subprocess
import time

def fileLocation():
    print("\nA calculation files with all of the equations and answers has"
       " been created here:")
    print("\033[92m" + f"{calcFileDirec}{fileName}" + "\033[0m")

def openFileLocation():
    subprocess.Popen(f'explorer "{calcFileDirec}"')

# clears the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def consoleSleep2():
    time.sleep(2)