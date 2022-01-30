def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)


n=int(input("Enter the number: "))
if n<=0:
    print("Enter the whole numbers")
else:
    for i in range(n):
        x=fib(i)
        print(x)
