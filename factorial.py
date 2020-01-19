

import sys
sys.getrecursionlimit()
sys.setrecursionlimit(200)
print(sys.getrecursionlimit())

def fact(n):
    a=1
    for i in range(n):
        c=n-i;
        a=a*c
        print(c,"!",end=' ')

    print()
    print(a)




fact(int(input("Please Enter the Number")))



