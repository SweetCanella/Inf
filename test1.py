def f(x):
    return 0.25 * x**3 + x - 2

a=1
b=2

fa=f(a)
fb=f(b)

while True:
    x = (a+b)/2
    if f(x)*fa>0:
        a=x
        fa=f(x)
    else:
        b=x
        fb=f(x)
    if 0.01 > abs((b-a)/x):
        break

print(f(x),x)