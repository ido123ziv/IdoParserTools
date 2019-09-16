import json
import sys
import os
import datetime
import time
from argparse import ArgumentParser
import subprocess
import logging

# general function  all the files are using the function name are self explained most of the time do not  worry .

def BytsToMB(byts):
    return byts/1000000


# check if the obj is json or the id

def IsJsonFile(jsonfile):
    try:
        with open(jsonfile) as date_file:
            pass
    except:
        return False
    return True


def print_error(msg):
    print ("\nERROR: {}\n".format(msg))
    sys.exit(1)


def makedir(path):
    try:
        os.makedirs(path)
    except OSError:
        print_error("dir exists")


# zip fill and delete file are both using bash commend
def zipfils(filspath):
    bashCommand = "zip -r " + filspath + '.zip ' + filspath
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    logging.info("zip file " + filspath + 'into ' + filspath + '.zip')


def printdir(dirpath):
    bashcommand = "ls " + dirpath
    os.system(bashcommand)

 # return a list of all the files in a dir for backups
def getdirfiles(dirpath):
    return os.listdir(dirpath)


def findfile(serchdir, filename):
    bashcommand = "find " + serchdir + " -name " + filename + " -print"
    # to add in the future -  | awk '{gsub('" + serchdir + "', "");print}'"
    os.system(bashcommand)


def findfileindir(dir, sfile):
    for r, d, f in os.walk(dir):
        for file in f:
            if sfile in file:
                return file


def filsize(filpath):
   filesize = os.stat(filpath)
   return BytsToMB(filesize.st_size)


def deletefile(filspath):
    bashCommand = "rm -r " + filspath
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    logging.warning("file deleted  " + filspath + '!!!! if there are not any logs indicated on zip pleas investigate')


# get dashboard backup file and return the backup dir
def GetDir(path):
    p = GetFullPath(path)
    p = os.path.dirname(p)
    return p


def GetFullPath(file):
    return os.path.abspath(file)


# all the time function are using in the logs or the file format pleas do not change
def GetTime():
    time = datetime.datetime.now()
    time = time.strftime("%Y-%m-%d")
    return time


def GetAccurateTime():
    time = datetime.datetime.now()
    bigtime = GetTime()
    smalltime = time.strftime("%H:%M:%S")
    accuratetime = bigtime + "|" + smalltime
    return  accuratetime


# the basic fun to create a lod bar
def lodingbar():
    toolbar_width = 40
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width + 1))  # return to start of line, after '['
    var = "meron"
    for i in range(toolbar_width):  # range should replace by the real condition
        time.sleep(0.1)  # do real work here
        # update the bar
        sys.stdout.write("|")
        sys.stdout.flush()

    sys.stdout.write("]\n")
    
    
def printNiceJSON(file_name):
  with open(file_name,'r+') as file1:
    list = json.load(file1)
  with open(file_name,'w+') as file1:
    json.dump(list,file1,indent=4,sort_keys=True)

