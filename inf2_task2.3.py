def f(a,b,c):
    d = b**2 - 4*a*c
    if d < 0:
        return 'nope'
    x1 = (-b + d**0.5)/(2*a)
    x2 = (-b - d**0.5)/(2*a)
    return x1,x2

a = int(input())
b = int(input())
c = int(input())
print(f(a,b,c))