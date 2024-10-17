from math import *

def f(x):
    return (cos(exp(1)*x))**3 + sin(abs(x))

a = int(input())
b = int(input())
h = int(input())
x=a
for x in range(a,b+1,h*x):
    print(f(x))
#неправильно считает??