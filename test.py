
def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        if(c<=100):
            print(c)
        else:
            break




fib(int(input("Please enter the Number")))