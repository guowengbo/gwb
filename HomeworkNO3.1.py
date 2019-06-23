import os

def eachFile(filepath):               
    pathDir =os.listdir(filepath) 
    return pathDir

def readfile(res1):                   
    fopen=open(res1,'r')
    for lines in fopen.readlines():      
        lines = lines.replace("\n", "").split(",")
        if 'http' in str(lines) or 'https' in str(lines): 
           print(lines)
    fopen.close()

filePath = "C:\Users\Administrator\Desktop\res1"
pathDir=eachFile(filePath)
for allDir in pathDir:
    child = "C:\Users\Administrator\Desktop\res1"  + allDir
    readfile(child)

