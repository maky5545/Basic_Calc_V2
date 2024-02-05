import os
import subprocess
from datetime import datetime
from Misc import consoleSleep2

userName = os.getlogin()
dateAndTime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
calcFileDirec = (f"C:\\Users\\{userName}\\Documents\\Python Files\\Basic Calculator\\Operations\\")
checkDirecExists = os.path.isdir(calcFileDirec)
fileName = f"calc_{dateAndTime}.txt"
textCounter = 0
lineCounter = 1
tryMakeDir = 0
tryFindDir = 0

# Create Log Files and write output to them
def outputFileCreator(value1, value2, operation, answer):
    global lineCounter
    global textCounter
    global tryMakeDir
    global createFile
    global tryFindDir
    
    if checkDirecExists == False:
        while True:
            try:
                os.makedirs(calcFileDirec, 0o777, exist_ok=False)
                break                
            except FileExistsError:
                if tryMakeDir < 3:
                    print("Code Failed: directory already exists! Trying again...")
                    tryMakeDir += 1
                    consoleSleep2()
                else:
                    print("Code Failed: directory already exists! Exiting...")
                    consoleSleep2()
                    exit()
                            
    elif checkDirecExists == True:
        while True:
            try:
                createFile = open(calcFileDirec + fileName, "w")
                createFile.close()
                break
            except FileNotFoundError:
                if tryFindDir < 3:
                    print("Directory not found! Trying again...")
                    consoleSleep2()
                else:
                    print("Directory not found! Exiting...")
                    consoleSleep2()
                    exit()
    
    while textCounter == 0:
        createFile = open(calcFileDirec + fileName, "a")
        createFile.write(f"{str(lineCounter)}. {value1} {operation} {value2} = {answer} \n")
        createFile.close()
        textCounter += 1
        lineCounter += 1
        break
    while textCounter > 0:
        createFile = open(calcFileDirec + fileName, "a")
        createFile.write(f"\n{str(lineCounter)}. {value1} {operation} {value2} = {answer} \n")
        createFile.close()
        lineCounter += 1
        break

def fileLocation():
    print("\nA calculation files with all of the equations and answers has"
       " been created here:")
    print("\033[92m" + f"{calcFileDirec}{fileName}" + "\033[0m")

def openFileLocation():
    subprocess.Popen(f'explorer "{calcFileDirec}"')
