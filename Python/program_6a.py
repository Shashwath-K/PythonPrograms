import os.path
import sys
fname=input("Enter the file name: ")

if not os.path.isfile(fname):
    print("File ",fname," doesn't exit")
    sys.exit(0)
infile=open(fname,"r")
lineList=infile.readlines()

for i in range(7):
    print(i+1," : ",lineList[i])
word=input("Enter a word: ")
cnt=0
for line in lineList:
    cnt+=line.count(word)
print("The word ",word," appears ",cnt," times in the file")
