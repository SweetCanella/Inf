from math import *

def f(x,y):
    if (x+y)<=2:
        return pow(sin(x*exp(0.1*y)),1/3)
    return abs(log(x+y,2))

for x in range(1,6):
    for y in range(1,5):
        print(f(x/2,y))