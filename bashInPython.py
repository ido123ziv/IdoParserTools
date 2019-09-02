import os
import sys
from pathlib import Path
'''How to find your current path using pycharm:'''

print("Directory Path:", Path().absolute())

'''how to find file using python:'''
print("File      Path:", Path(__file__).absolute())

'''how to find the file folder:'''
sys.stdout.write(f"Directory     Path: {Path(__file__).resolve().parent}\n")

'''how to write to console:'''
sys.stdout.write(f"File      Path: {Path().absolute()}\n")

'''
find current directory
#sys.stdout.write("Directory Path:", Path().absolute())
dirOfProject = Path(__file__).resolve().parent

'''
myDir = "/home/mgs-dev/PycharmProjects/IdoCentos/"
userInput = myDir + "userInput.json"
dbFile = myDir + 'notification.db'

'''address files'''
userInput = dirOfProject / "userInput.json"
dbFilePath = dirOfProject / 'notification.db'
dbFile = str(dbFilePath)
