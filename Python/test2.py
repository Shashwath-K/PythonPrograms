n=input("Enter a string: ")
str_val=str(n)
if str_val==str_val[::-1]:
    print("Given string is palindrome: ",n)
else:
    print("Not a palindrome")
    
for i in range(10):
    if str_val.count(str(i))>0:
        print(str(i),"appears",str_val.count(str(i)),"times")
