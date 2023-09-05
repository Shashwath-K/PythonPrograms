def bin2dec(n):
    rev=n[::-1]
    dec=0
    i=0
    for dig in rev:
        dec +=int(dig)*2**i
        i+=1
    return dec
n1=input("Enter number in binary: ")
print(bin2dec(n1))

def oct2dec(n):
    rev=n[::-1]
    dec=0
    i=0
    for dig in rev:
        dec +=int(dig)*8**i
        i+=1
    hex_list=[]
    while dec!=0:
        hex_list.append(dec%16)
        dec=dec//16
    n1=[]
    for elem in hex_list[::-1]:
        if elem<=9:
            n1.append(str(elem))
        else:
            n1.append(chr(ord('A')+(elem-10)))
        hex_value="".join(n1)
    return hex_value
n2=input("Enter a octal number: ")
print(oct2dec(n2))
