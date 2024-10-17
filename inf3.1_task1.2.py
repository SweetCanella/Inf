from math import *

def f(x,y):
    if sin(x+y)<=-0.5:
        return atan(pow(abs(x-y),1/3))*(x*exp(y))
    elif sin(x+y)<0.5:
        return 3*log(abs(x*y),3)
    else:
        return x**3+y**1.5

x = int(input())
y = int(input())
print(f(x,y))
