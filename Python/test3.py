def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
n=int(input("Enter the value of n: "))
if(n==0):
    exit
else:
    print("Fibonacci sequence of the number :", fib(n))