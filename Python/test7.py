def romToDec(romNum):
    dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    romBack=list(romNum)[::-1]
    value=0
    right_val=dic[romBack[0]]
    for numeral in romBack:
        left_val=dic[numeral]
        if left_val<right_val:
            value-=left_val
        else:
            value+=left_val
            right_val=left_val
    return value
n=input("Enter the roman value: ")
print("The Decimal value of the given roman number is: ",romToDec(n))