m1=int(input("Enter the marks of test 1: "))
m2=int(input("Enter the marks of test 2: "))
m3=int(input("Enter the marks of test 3: "))

if(m1<m2 and m1<m3):
    avg=(m2+m3)/2
elif(m2<m1 and m2<m3):
    avg=(m1+m3)/2
else:
    avg=(m1+m2)/2

print("Average of two test results: ",avg)