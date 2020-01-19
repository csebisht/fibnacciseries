

from functools import reduce

def even(n):
    return n%2==0
num=[1,2,3,4,5,6,7,9]
evens=list(filter(even,num))
print(evens)
add2=reduce(lambda c,f:c+f,evens)
print(add2)
Elist=list(filter(lambda a : a%2==0,range(20)))
print(Elist)
add1=reduce(lambda c,f:c+f,Elist)
print(add1)

elits=list(map(lambda b : b*2,range(20)))
print(elits)

add=reduce(lambda c,f:c+f,elits)
print(add)