from math import *

def f(x):
    return (cos(exp(1)*x))**3 + sin(abs(x))

a = int(input())
b = int(input())
h = int(input())
for x in range(a,b+1,h):
    print(f(x))
#неправильно считает??