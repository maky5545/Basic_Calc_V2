import os
import time
from datetime import datetime

userName = os.getlogin()
dateAndTime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
dateAndTimeNow = str(dateAndTime)
calcFileDirec = (f"C:\\Users\\{userName}\\Documents\\Python Files\\Basic Calculator\\Operations\\")
checkDirecExists = os.path.isdir(calcFileDirec)
folderCreationLoop = False
fileCreationLoop = False
fileName = f"calc_{dateAndTime}.txt"
textCounter = 0
lineCounter = 1

# Check if the number has a decimal part
def noDecimal(inoCheck):
    if inoCheck % 1 == 0:
        return True
    elif inoCheck % 1 != 0:
        return False

# Check if directory and file exsists, if not, create them, then write the values to the files.
def fileCreator(value1, value2, operation, answer):
    global folderCreationLoop
    global fileCreationLoop
    global fileCreated
    global createFile
    global textCounter
    global lineCounter
    if checkDirecExists == False:
        while folderCreationLoop == False:
            try:
                os.makedirs(calcFileDirec, 0o777, exist_ok=False)
                folderCreationLoop = True
            except FileExistsError:
                print("Code Failed: directory already exists! Exiting...")
                folderCreationLoop = False
                time.sleep(5)
                exit()

            time.sleep(0.5)
    elif checkDirecExists == True:
        while fileCreationLoop == False:
            try:
                createFile = open(calcFileDirec + fileName, "x")
                createFile.close()
                fileCreationLoop = True
                fileCreated = True
            except:
                print("Temp String")
                input("")
    
    if textCounter == 0:
        createFile = open(calcFileDirec + fileName, "a")
        createFile.write(f"{str(lineCounter)}. {value1} {operation} {value2} = {answer} \n")
        createFile.close()
        fileCreated = False
        textCounter += 1
        lineCounter += 1
    elif textCounter > 0:
        createFile = open(calcFileDirec + fileName, "a")
        createFile.write(f"\n{str(lineCounter)}. {value1} {operation} {value2} = {answer} \n")
        createFile.close()
        lineCounter += 1



