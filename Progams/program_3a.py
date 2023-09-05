n=input("Enter the sting: ")
wordlist=n.split(" ")
up=lo=dig=0
for ch in n:
    if "0" <=ch <="9":
        dig+=1
    if "A" <=ch <="Z":
        up+=1
    if "a" <=ch<="z":
        lo+=1
print("The number of Digits: ",dig,"\nThe number of uppercase letters: ",up,"\nThe number of lowercase letters: ",lo,"\nThe number of words: ",len(wordlist))