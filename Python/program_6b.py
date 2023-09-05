import os
import sys
import pathlib
import zipfile

dirName=input("Enter the directory name: ")

if not os.path.isdir(dirName):
    print("Directory",dirName,"doesn't exist")
    sys.exit(0)

curDir=pathlib.Path(dirName)

with zipfile.ZipFile("myzip.zip",mode="w")as archive:
    for file_path in curDir.rglob("*"):
        archive.write(file_path,arcname=file_path.relative_to(curDir))

if os.path.isfile("myzip.zip"):
    print("Archive","myzip.zip","created successfully")
else:
    print("Error in creating zip archive")
